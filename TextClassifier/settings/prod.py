from TextClassifier.settings.base import *

# Override base.py settings here
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': 'ec2-54-204-21-226.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
