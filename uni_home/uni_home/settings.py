"""
Django settings for uni_home project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

import os
import cloudinary_storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9nor@w)_1#3d!p2-sph+9zx^z2@=+4mdp$x-de#(n5#jy=de9v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'uniaway-61bad5bc656e.herokuapp.com',
    '127.0.0.1',
    'www.uniaway.it',
    'uniaway.it',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'phonenumber_field',
    'storages',
    'cloudinary_storage',



]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uni_home.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'uni_home.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
   # 'default': {
      #  'ENGINE': 'django.db.backends.postgresql',
      #  'NAME': 'de9iit4vdjjacl',
       # 'USER': 'nrvoofexohvwwg',
      #  'PASSWORD': '728b226bd134466892fb1e8a48577abe21d670e67d5d7981bbc0288c5136ddcd',
       # 'HOST': 'ec2-99-80-246-170.eu-west-1.compute.amazonaws.com',
       # 'PORT': '5432',
 #   }
#}

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
       # 'NAME': BASE_DIR / 'db.sqlite3',
   # }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dfa9q7ph2v3cc8',
        'USER': 'hcbtxyhrxdkauk',
        'PASSWORD': '0a0ae117969855a297b3cc9184206aa945bd789d9832720d5d6292b30dd4006c',
        'HOST': 'ec2-54-195-120-0.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
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
if DEBUG:
     STATICFILES_DIRS=(
        os.path.join(BASE_DIR, 'static'),
         )
else:
     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
#MEDIA_URL = 'https://uniaway.s3.amazonaws.com/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#STATIC_URL = 'https://uniaway.s3.amazonaws.com/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# media file

# MEDIA_URL = '/media/'


# gmail config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'unicasa.help@gmail.com'
EMAIL_HOST_PASSWORD = 'rxbamezrbusnfclg'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SECURE_SSL_REDIRECT = True

LOGIN_URL = '/host_landing/'


#AWS_ACCESS_KEY_ID = 'AKIA424VTZC45NSNFKIG'
#AWS_SECRET_ACCESS_KEY = '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'
#AWS_STORAGE_BUCKET_NAME = 'uniaway'
#AWS_S3_SIGNATURE_NAME = 's3v4'
#AWS_S3_REGION_NAME = 'eu-central-1'
#AWS_S3_FILE_OVERWRITE = False
#AWS_DEFAULT_ACL = None
#AWS_S3_VERIFY = True
#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dwvrhsdym',
    'API_KEY': '581651649529242',
    'API_SECRET': '7kbO0_RfzSxqaBG-EGa5HV4Uibg'
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'