django-C3PO
=============
django-C3PO is a Django application using C3PO - module responsible for converting .po files from locale folder
with translations to .ods format and sending them to Google Spreadsheets.

This Django application provides panel where user can synchronize translations with GDocs and it gives
possibility to push all translations on git and checkout last commit.

After synchronization django-C3PO sends post_compilemessages signal which notifies that translations are ready.
Server restart is needed then to reload compiled .mo files into application.

Application uses celery to prevent timeout when synchronizing translations.
Be sure to properly configure it before use.

django-C3PO includes custom compilemessages command called verbosecompilemessages.
It is needed to write msgfmt errors on the stderr, because standard compile messages
does not show them.

Quick start
-----------

1. Add "django-C3PO" to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = (
    ...
    'django_c3po',
)
```

2. Add C3PO variable to your settings and define them. For example:

```python
C3PO = {
    'LANGUAGES': ['en', 'pl', 'jp'],
    'EMAIL': 'ttestt123321@gmail.com',
    'PASSWORD': 'zxcasdqwe.',
    'URL': 'https://docs.google.com/spreadsheet/ccc?key=0AnVOHClWGpLZdGRuQVlrWG5Ia3QtOHJEWWpmZVYyYnc#gid=0',
    'HEADER': '# translated with po_translator\n',
    'LOCALE_ROOT': os.path.join('conf', 'locale'),
    'PO_FILES_PATH': 'LC_MESSAGES',
    'TEMP_PATH': 'temp',
    'GIT_REPOSITORY': 'git@git.hiddendata.co:mnogacki/testpo.git',
    'GIT_BRANCH': 'master',
    'SOURCE': 'PO Translator',
}
```

3. Include the po_translator URLconf in your project urls.py like this::

```python
url(r'^c3po/', include('django_c3po.urls')),
```

4. Add post_compilemessages signal receiver for server restart:
```python
@receiver(post_compilemessages)
def restart_server_callback(sender, *args, **kwargs):
    manage_path = os.path.join(settings.ROOT_DIR, '..', 'manage.py')
    os.system('touch ' + manage_path)
```

5. Configure celery in your settings:
```python
BROKER_URL = 'django://'
CELERY_IMPORTS = ('test_app.models',)

import djcelery
djcelery.setup_loader()
```
Be sure to include module with your signal receiver in CELERY_IMPORTS.

6. Start the development server, visit http://127.0.0.1:8000/admin/
   and add permission 'django-C3PO.can_translate' to user.

7. Visit http://127.0.0.1:8000/c3po/ and log in as user with can_translate permission.

8. Use buttons to synchronize, make messages and git operations.
-
Usage
-----
After configuration and logging into the translator's panel, you will see basic configuration info with
link to the spreadsheet defined in settings. User can manage app translations with three actions:

 - Synchronize - Synchronized translations from local files with GDoc state. If project has new expressions
   which are not in the spreadsheet, GDoc is updated with this entries. Remember that after this action server
   should be restarted.
 - Make messages - Runs makemessages command updating po files with new expressions to translate.
 - Publish - Pushes current po files to git repository.
 - Reset - Reverts current changes and checkouts project to last commit. Note that changes are also reverted
   in spreadsheet, so all new translations will be lost.
