#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from django.conf import settings
from django.dispatch.dispatcher import receiver
from django_c3po.signals import post_compilemessages


@receiver(post_compilemessages)
def restart_server_callback(sender, **kwargs):
    manage_path = os.path.join(settings.ROOT_DIR, '..', 'manage.py')
    os.system('touch ' + manage_path)
