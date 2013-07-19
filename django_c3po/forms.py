#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms


class TranslationForm(forms.Form):
    git_message = forms.CharField(max_length=255)
