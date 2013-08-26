#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

from django.contrib.auth.decorators import permission_required
from django.conf import settings
from django.core import management
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from signals import post_compilemessages

from c3po.mod.communicator import Communicator, git_push, git_checkout, PODocsError


log = logging.getLogger('django_c3po')

email = settings.C3PO['EMAIL']
password = settings.C3PO['PASSWORD']
url = settings.C3PO['URL']
source = settings.C3PO['SOURCE']
temp_path = settings.C3PO['TEMP_PATH']
languages = settings.C3PO['LANGUAGES']
locale_root = settings.C3PO['LOCALE_ROOT']
po_files_path = settings.C3PO['PO_FILES_PATH']
header = settings.C3PO['HEADER']
git_repository = settings.C3PO['GIT_REPOSITORY']
git_branch = settings.C3PO['GIT_BRANCH']
login_url = settings.C3PO['LOGIN_URL']


class IndexView(TemplateView):
    template_name = 'django_c3po/index.html'

    actions_allowed = ['synchronize', 'reset', 'makemessages', 'publish']

    @method_decorator(permission_required('django_c3po.can_translate', login_url=reverse_lazy(login_url)))
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        ret = super(IndexView, self).get_context_data(*args, **kwargs)
        ret['settings'] = settings.C3PO
        ret['error'] = self.request.session.pop('error', None)
        ret['info'] = self.request.session.pop('info', None)
        ret['logout_url'] = settings.C3PO['LOGOUT_URL']
        return ret

    def post(self, request, *args, **kwargs):
        action_name = request.POST['action']
        if action_name in self.actions_allowed:
            try:
                ret = getattr(self, action_name)(request, *args, **kwargs)
            except PODocsError as e:
                log.exception(e)
                error = e
            else:
                return ret
        else:
            error = PODocsError(_('Wrong action'))
        return self.render_podocs_response(request, error=error)

    def render_podocs_response(self, request, info=None, error=None, *args, **kwargs):
        request.session['error'] = error
        request.session['info'] = info
        return redirect('c3po_index')

    def synchronize(self, request, *args, **kwargs):
        communicator = Communicator(email, password, url, source, temp_path,
                                    languages, locale_root, po_files_path, header)

        if not os.path.exists(locale_root):
            os.makedirs(locale_root)

        communicator.synchronize()

        management.call_command('compilemessages', verbosity=0)

        post_compilemessages.send(sender=self)

        info = _('Translations synchronized')
        return self.render_podocs_response(request, info)

    def makemessages(self, request, *args, **kwargs):
        if not os.path.exists(locale_root):
            os.makedirs(locale_root)
        for lang in languages:
            management.call_command('makemessages', locale=lang, verbosity=0)

        info = _('Messages made for languages: ' + ', '.join(languages))
        return self.render_podocs_response(request, info)

    def publish(self, request, *args, **kwargs):
        git_message = request.POST['git_message']
        if git_message == '':
            error = _('Enter git message')
            return self.render_podocs_response(request, error=error)

        info, error = git_push(git_message, git_repository, git_branch, locale_root)

        return self.render_podocs_response(request, info, error)

    def reset(self, request, *args, **kwargs):
        communicator = Communicator(email, password, url, source, temp_path)

        info, error = git_checkout(git_branch, locale_root)
        communicator.upload(languages, locale_root, po_files_path)

        if info == '':
            info = _('Changes have been reverted')

        return self.render_podocs_response(request, info, error)
