#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-C3PO',
    version='0.0.1-dev',
    packages=['django_c3po'],
    url='http://www.hiddendata.co/',
    license='MIT',
    author=u'Marek Nogacki',
    author_email='m.nogacki@hiddendata.co',
    description='Django application for translators using c3po module',
    install_requires=['gdata==2.0.18', 'c3po==0.0.1'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    include_package_data=True,
)
