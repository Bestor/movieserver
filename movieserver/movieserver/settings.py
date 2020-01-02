import os

DEBUG = True

DIRNAME = os.path.abspath(os.path.dirname(__file__))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'movieserver'
]
SECRET_KEY = "THIS IS PROBABLY NOT SECURE BUT I JUST WANT IT TO RUN"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'registry/templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
            ],
            'debug': DEBUG,
        }
    }
]

MIDDLEWARE = ['django.contrib.auth.middleware.AuthenticationMiddleware',
              'django.contrib.messages.middleware.MessageMiddleware',
              'django.contrib.sessions.middleware.SessionMiddleware']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'movieservicedb',
        'USER': 'postgres',
        'PASSWORD': 'mysecretpassword',
        'HOST': 'josh-stack.vse.rdlabs.hpecorp.net',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '12345',  # Set to empty string for default.
    }
}

STATIC_ROOT = DIRNAME + '/static/'
STATIC_URL = '/static/'
ROOT_URLCONF = 'movieserver.urls'
