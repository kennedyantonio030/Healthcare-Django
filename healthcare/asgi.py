"""
ASGI config for healthcare project.

It exposes the ASGI callable as a module-level variable named ``application``.


https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings')

application = get_asgi_application()
