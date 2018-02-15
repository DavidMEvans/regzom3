from .base import *
import dj_database_url

DEBUG = False

DATABASES = {'default': dj_database_url.parse(os.environ.get('CLEARDB_DATABASE_URL')) }

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<STRIPE_PUBLISHABLE key>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<STRIPE_SECRET key>')

SITE_URL = 'https://regzom.herokuapp.com'
ALLOWED_HOSTS.append('regzom.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}