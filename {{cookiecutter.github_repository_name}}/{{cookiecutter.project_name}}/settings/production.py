from settings.common import *

DEBUG = False

LOGGING['handlers']['logentries'] = {
            'level': 'INFO',
            'token': os.environ.get("LOGENTRIES_KEY", ''),
            'class': 'logentries.LogentriesHandler',
            'formatter': 'verbose'
        }

LOGGING['loggers']['{{cookiecutter.project_name}}']['handlers'] = ['console', 'file', 'logentries']

{% if cookiecutter.use_celery == 'y' %}
########## CELERY
# In production, all tasks will be executed in the worker
CELERY_ALWAYS_EAGER = False
########## END CELERY
{% endif %}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')