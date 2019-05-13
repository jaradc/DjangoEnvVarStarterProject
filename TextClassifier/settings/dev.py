from TextClassifier.settings.base import *

# Override base.py settings here
DEBUG = True

# Log into Postgres as SuperUser
# psql -U postgres -h localhost -p 5432
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}