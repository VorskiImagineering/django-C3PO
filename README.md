django-C3PO
=============
django-C3PO is a Django application using C3PO - module responsible for converting .po files from locale folder
with translations to .ods format and sending them to Google Spreadsheets.

This Django application provides panel where user can synchronize translations with GDocs and it gives
possibility to push all translations on git and checkout last commit.

After synchronization django-C3PO sends post_compilemessages signal which notifies that translations are ready.
Server restart is needed then to reload compiled .mo files into application.

Quick start
-----------

1. Add "django-C3PO" to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = (
    ...
    'django-C3PO',
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
url(r'^c3po/', include('django-C3PO.urls')),
```

4. Start the development server, visit http://127.0.0.1:8000/admin/
   and add permission 'django-C3PO.can_translate' to user.

5. Visit http://127.0.0.1:8000/c3po/ and log in as user with can_translate permission.

6. Use buttons to synchronize, make messages and git operations.

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
