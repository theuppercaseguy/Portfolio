"""
Django settings for PORTFOLIO project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3vvuy1+!m9_2ym8*#(2n9hv&2o-ik$pk9!qbvrvd(*cz@w*jx%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pp',
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django_babel.middleware.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PORTFOLIO.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'PORTFOLIO.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'zslxiaoi',
    'USER':'zslxiaoi',
    'PASSWORD':'codkc8v-KfJs_W-ipT46NM51m0Eh--P6', 
    'HOST':'surus.db.elephantsql.com',
    'PORT': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),
]

# LOCALE_PATHS = [
#     os.path.join(BASE_DIR,'locale'),
# ]

MEDIA_ROOT = os.path.join(BASE_DIR,'/media/')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django_ses.SESBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '5432'
EMAIL_HOST_USER = 'saadan060@gmail.com'
EMAIL_HOST_PASSWORD = 'lucifermorningstar'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True


AWS_ACCESS_KEY_ID = 'AKIARSDMIO6TXGDMI2VD'
AWS_SECRET_ACCESS_KEY = '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'
AWS_SES_REGION_NAME = 'us-east-1' #(ex: us-east-2)
AWS_SES_REGION_ENDPOINT ='email.us-east-1.amazonaws.com' #(ex: email.us-east-2.amazonaws.com)


django_heroku.settings(locals())

