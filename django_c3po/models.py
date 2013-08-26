#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Translator(models.Model):
    """
    Model needed to add permissions to the User model.
    Permission defines whether user can synchronize translations in project.
    """

    class Meta:
        # abstract = True
        permissions = (
            ('can_translate', 'Can publish and retrieve translations'),
        )
