from settings import *

DEBUG = False

LOG_KEY = "{{cookiecutter.logentries_key}}"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(pathname)s %(lineno)d] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'logentries': {
            'level': 'INFO',
            'token': os.environ.get("LOGENTRIES_KEY", LOG_KEY),
            'class': 'logentries.LogentriesHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/{{ cookiecutter.app_name }}_logs.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'trackme': {
            'handlers': ['logentries', 'file'],
            'level': 'INFO',
            'propagate': True,
        }
    },
}
