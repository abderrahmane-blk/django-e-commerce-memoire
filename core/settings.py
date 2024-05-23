"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!io^9xk)29l0%#uzh)g1ok0rg(qf2v57igfgf9=4x9!!4za#39'

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
    'paypal.standard.ipn',
    'chargily_epay_django',

    'corsheaders',

    'accounts',
    'store',
    'finance',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'memoire',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # 'localhost' if MySQL runs on the same machine
        'PORT': '3306',  # Default MySQL port
    }
}








# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = 'static/'
#abdu : good , could be changed if you don't like it
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

MEDIA_URL ='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Use database backend






# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL='dashboard'
LOGOUT_REDIRECT_URL='login'


PAYPAL_RECEIVER_EMAIL ='memoireUS@business.example.com'     #here the money goes ; then we send to each vendor his money after he accomplishes his work

PAYPAL_TEST =True
PAYPAL_EMAIL ='memoireUS@business.example.com'     #here the money goes ; then we send to each vendor his money after he accomplishes his work

# chargili
CHARGILY_KEY = "test_pk_kBHjwoMaV8CUb1TrA9gQIcbIF8QLsaeG8QKBkcNQ"
CHARGILY_SECRET = "test_sk_H1OYCPmSsKac9gp1gw2y5Uqp4ZVpvIA6TXvn44R1"
CHARGILY_URL = "https://pay.chargily.net/test/api/v2/"


CHARGILY_API_KEY ="test_pk_kBHjwoMaV8CUb1TrA9gQIcbIF8QLsaeG8QKBkcNQ"
CHARGILY_SECRET_KEY = "test_sk_H1OYCPmSsKac9gp1gw2y5Uqp4ZVpvIA6TXvn44R1"

CHARGILY_FAKE_DOMAIN = "https://pay.chargily.net/test/api/v2"
# CHARGILY_SITE


# https://pay.chargily.net/test/api/v2



CORS_ALLOW_ALL_ORIGINS = True