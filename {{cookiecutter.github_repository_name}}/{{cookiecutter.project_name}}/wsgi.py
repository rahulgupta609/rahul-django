"""
WSGI config for {{ cookiecutter.project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
{% if cookiecutter.use_newrelic == 'y' %}
import newrelic.agent
{% endif %}
from django.core.wsgi import get_wsgi_application

PROJECT_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_name}}.settings.production")

{% if cookiecutter.use_newrelic == 'y' %}
# Initializes the new relic agent
NEWRELIC_CONFIG_FILE = os.path.join(PROJECT_DIR, "{{cookiecutter.project_name}}/newrelic.ini")
newrelic.agent.initialize(NEWRELIC_CONFIG_FILE)
{% endif %}

application = get_wsgi_application()

{% if cookiecutter.use_newrelic == 'y' %}
application = newrelic.agent.wsgi_application()(application)
{% endif %}
