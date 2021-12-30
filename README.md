# Django + DRF playground

## Admin credentials

- username: admin
- password: password1234

## Django cheatsheet

`python manage.py startapp polls`

`python manage.py createsuperuser`

## black + pycharm

https://black.readthedocs.io/en/stable/integrations/editors.html

1. Make sure you have the File Watchers plugin installed.

2. Go to Preferences or Settings -> Tools -> File Watchers and click + to add a new watcher:

    Name: Black

    File type: Python

    Scope: Project Files

    Program: <install_location_from_step_2>

    Arguments: $FilePath$

    Output paths to refresh: $FilePath$

    Working directory: $ProjectFileDir$

3. In Advanced Options

    Uncheck “Auto-save edited files to trigger the watcher”

    Uncheck “Trigger the watcher on external changes”