from .base import *
import dj_database_url

DEBUG = False

DATABASES = {'default': dj_database_url.config('mysql://b91a1de1322310:d6bc7f41@eu-cdbr-west-02.cleardb.net/heroku_40c76d061922b57?')
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<STRIPE_PUBLISHABLE key>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<STRIPE_SECRET key>')

# Paypal environment variables
#PAYPAL_NOTIFY_URL = 'https://291e2d8f.ngrok.io/a-very-hard-to-guess-url/'
#PAYPAL_RECEIVER_EMAIL = 'aaron@codeinstitute.net'

SITE_URL = 'https://regzom.herokuapp.com'
ALLOWED_HOSTS.append('https://regzom.herokuapp.com')

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