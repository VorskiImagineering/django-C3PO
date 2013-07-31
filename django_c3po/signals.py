#!/usr/bin/env python
# -*- coding: utf-8 -*-

import django.dispatch

# Signal to inform application about ready .mo files, so server will know when to restart itself.
post_compilemessages = django.dispatch.Signal()
