"""
    Django settings for planetchallenge_project project.
"""
import sys
import os
import dj_database_url
from pathlib import Path
import dotenv
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load enviroment .env
dotenv_path = os.path.join(BASE_DIR, '.env')
dotenv.load_dotenv(dotenv_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJ_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1', '']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'corsheaders',
    'storages',

    'rest_framework',
    'rest_framework.authtoken',

    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # https://stackoverflow.com/questions/59230539/django-rest-swagger-staticfiles-is-not-a-registered-tag-library-must-be-one
    # 'rest_framework_swagger',
    'drf_spectacular',

    'core',
    'auth_api',
    'game_api',
    'trivia_api',
    'player_api',

    'django_filters',
    'django_extensions'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'planetchallenge_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # ref. views project
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

WSGI_APPLICATION = 'planetchallenge_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

# This setting tells Django at which URL static files are going to be served to the user.
# Here, they will be accessible at your-domain.onrender.com/static/...
STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

if not DEBUG:  # Tell Django to copy statics to the `staticfiles` directory
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/images')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'core.User'

# Default storage in aws
AWS_QUERYSTRING_AUTH = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', default='')

AWS_STORAGE_BUCKET_NAME = 'climatechallenge'

# Cors configuration
CORS_ALLOW_ALL_ORIGINS = True  # If this is used then `CORS_ALLOWED_ORIGINS`
                                # will not have any effect
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']


# Testing colors
# https://stackoverflow.com/questions/7815513/colorizing-the-output-of-django-tests
TEST_RUNNER = "redgreenunittest.django.runner.RedGreenDiscoverRunner"

# Rest framework configuration
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),

    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'core.serializers.UserSerializer',
}

REST_AUTH = {
    'USE_JWT': True,
}

SITE_ID = 1  # https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional
REST_USE_JWT = True  # use JSON Web

# Specular settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'PlanetChallengeAPI',
    'DESCRIPTION': '🔖 RESTful JSON API for Planet Challenge a Unity game.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'APPEND_COMPONENTS': {
        "securitySchemes": {
            "ApiKeyAuth": {
                "type": "apiKey",
                "in": "header",
                "name": "Authorization"
            }
        }
    },
    'SECURITY': [{"ApiKeyAuth": [], }]
}

# Social authentication configuration
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
            "openid",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "VERIFIED_EMAIL": True,
    }
}

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    "USER_ID_FIELD": "userId",  # for the custom user model
    "USER_ID_CLAIM": "user_id",
    "SIGNING_KEY": os.getenv('JWT_SECRET_KEY')
}

# dj-rest-auth settings
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
