#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractBaseUser


class Translator(AbstractBaseUser):

    class Meta:
        abstract = True
        permissions = (
            ('can_translate', 'Can publish and retrieve translations'),
        )
