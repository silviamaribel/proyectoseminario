"""
Django settings for proyectojuego project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#RUTA_PROYECTO=os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g@gtp*rf7dz37)li7aqrfc2mijrz9*+mhc@&602$yfuw@9b9e-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proyectojuego.apps.inicio',
    'captcha',
    'social.apps.django_app.default',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'proyectojuego.urls'

WSGI_APPLICATION = 'proyectojuego.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'triviadjango',
        'HOST':'127.0.0.1',
        'USER':'root'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#facebook
TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT=os.path.join(BASE_DIR,'proyectojuego/media')
TEMPLATE_DIRS=(os.path.join(BASE_DIR,'proyectojuego/templates'),)
STATICFILES_DIRS=(os.path.join(BASE_DIR,'proyectojuego/static'),)

RECAPTCHA_PUBLIC_KEY = '6Lf9cv0SAAAAAJXUjVL_ZUzbWCcIeex_uwsfcHvV'
RECAPTCHA_PRIVATE_KEY = '6Lf9cv0SAAAAAIN8n2qbdkCyqy0sCOUfLQ5OfvCf'

AUTHENTICATION_BACKENDS=(
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    )
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/user/perfil/'

SOCIAL_AUTH_FACEBOOK_KEY='822407231115641'
SOCIAL_AUTH_FACEBOOK_SECRET='0c1ef53b2858268bd2904e6f8f63b6ea'

LOGIN_URL          = '/login/' #url de la pagina de login del sistema
LOGIN_REDIRECT_URL = '/user/perfil/' #urla la que se enviara despues del login
LOGIN_ERROR_URL    = '/login-error/' #url si existe errores

