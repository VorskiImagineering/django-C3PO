#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-C3PO',
    version='0.2.2',
    packages=['django_c3po'],
    url='https://github.com/VorskiImagineering/django-C3PO',
    license='MIT',
    author=u'Marek Nogacki',
    author_email='m.nogacki@hiddendata.co',
    description='''django-C3PO is a Django application using C3PO - module
    responsible for converting .po files from locale folder with translations
    to .ods format and sending them to Google Spreadsheets.\n
    This Django application provides panel where user can synchronize
    translations with GDocs and it gives possibility to push all translations
    on git and checkout last commit.\n
    django-C3PO uses celery since version 0.2. Be sure to properly configure
    it before using application.''',
    install_requires=['django==1.5.1', 'gdata==2.0.18', 'c3po==0.2.0',
                      'celery==3.0.23', 'django-celery==3.0.23'],
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
    download_url='https://github.com/VorskiImagineering/django-C3PO/tarball/master',
)
