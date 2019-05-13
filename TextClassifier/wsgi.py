"""
WSGI config for TextClassifier project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# NOTE: I set this to None because I'm setting this environment variable in
# dev and prod so None should NEVER happen since it's the fall-back value.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', None) # 'TextClassifier.settings.prod'

application = get_wsgi_application()
