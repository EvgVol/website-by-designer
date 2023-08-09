from pathlib import Path

from decouple import Csv, config
from dotenv import load_dotenv


load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool, default=True)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default='127.0.0.1')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES_DIR = BASE_DIR / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Samara'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', cast=str, default='your-email@yandex.ru')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', cast=str, default='your-password')
EMAIL_SERVER = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = config('EMAIL_ADMIN', cast=str, default=['your-email@yandex.ru'])

TELEGRAM_TOKEN = '5809864142:AAGZ-v9svwFOS5gWOMrHo6tsIO70kwJmXLk'
TELEGRAM_CHAT_ID = '1091123046'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            '()': 'dockerflow.logging.JsonLogFormatter',
            'logger_name': 'myapp',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'json',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'myapp': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
