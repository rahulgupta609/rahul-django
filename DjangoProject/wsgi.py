"""
WSGI config for DjangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
from __future__ import unicode_literals, absolute_import
import os

import newrelic.agent

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject.settings.production")

application = get_wsgi_application()


# Initialize the new relic agent
PROJECT_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
NEWRELIC_CONFIG_FILE = os.path.join(PROJECT_DIR, "DjangoProject/newrelic.ini")
newrelic_env = os.environ.get("DJANGO_SETTINGS_MODULE")

if newrelic_env:
    # convert DjangoProject.settings.environment to environment
    newrelic_env = newrelic_env.split(".")[-1]
    newrelic.agent.initialize(NEWRELIC_CONFIG_FILE, newrelic_env)
else:
    newrelic.agent.initialize(NEWRELIC_CONFIG_FILE)

application = newrelic.agent.wsgi_application()(application)

