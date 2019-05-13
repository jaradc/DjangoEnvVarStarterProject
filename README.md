# Django Starter Project

A Django project using environment variables, PostgreSQL and separate settings.

## Prerequisites

 1. Setup a PostgreSQL database locally. Assuming you have PGAdmin installed, in terminal, you can `psql -U postgres -h localhost -p 5432` then use this command to create the database `CREATE DATABASE somedbname OWNER whoever;` where "somedbname" is the name of the database and "whoever" is a user you want to define as the owner.
 2. In your virtual environment, find `Scripts/activate.bat` to set environment variables at the **top** of the file like this:
     ```
     @echo off

    set "DJANGO_SETTINGS_MODULE=TextClassifier.settings.dev"
    set "SECRET_KEY=_fif-!e8&jz@db@&(4pir)ftqg%+)9&-365hb1f)@&$^9pst4_"
    set "DATABASE_NAME=somedbname"
    set "DATABASE_USER=whoever"
    set "DATABASE_PASSWORD=abc123"
    ```
 3. Find `Scripts/deactivate.bat` and unset the environment variables like this:
     ```
     @echo off
     
    set DJANGO_SETTINGS_MODULE=
    set SECRET_KEY=
    set DATABASE_NAME=
    set DATABASE_USER=
    set DATABASE_PASSWORD=
     ```
     
    ### The Environment Variables
    **DJANGO_SETTINGS_MODULE**: This tells Django what settings file to use. Look at your project's wsgi.py file. Notice how this variable is being set. [Source](https://docs.djangoproject.com/en/2.2/topics/settings/#designating-the-settings)
    
    **SECRET_KEY**: The Django secret key that you want to protect.
    
    **DATABASE_NAME**: The name of your PostgreSQL database.
    
    **DATABASE_USER**: Your PostgreSQL username.
    
    **DATABASE_PASSWORD**: Your PostgreSQL password.
    

## Notes

Create a `settings` directory and move settings.py into this directory and rename it to `base.py`. Add an `__init__.py` file to this directory. Now create `dev.py` and `prod.py`. In these files, you will keep environment-specific settings.

**Remember:** The DJANGO_SETTINGS_MODULE environment variable is telling Django whether to use the `yourproject.settings.dev` or `yourproject.settings.prod`.
    
    Your settings directory should look like this:
    
    ```
    settings
     - __init__.py
     - base.py
     - dev.py
     - prod.py
     ```