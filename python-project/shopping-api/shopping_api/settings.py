import os
from os.path import join
from pathlib import Path

from dj_database_url import parse as parse_db_url
from prettyconf import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=config.boolean)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*", cast=config.list)

# Django apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third-party apps
    "rest_framework",
    "rest_framework.authtoken",
    "django_extensions",
    # apps
    "apps.commons",
    "apps.products",
    "apps.clients",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Template config
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
STATIC_URL = "/static/"

# Route/HTTP config
ROOT_URLCONF = "shopping_api.urls"
WSGI_APPLICATION = "shopping_api.wsgi.application"
HTTPS_REQUIRED = config("HTTPS_REQUIRED", default=True, cast=config.boolean)

# Time config
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# DB
DATABASES = {"default": config("DATABASE_URL", cast=parse_db_url)}
if DEBUG:
    DATABASES["default"]["TEST"] = {"NAME": config("TEST_DATABASE_NAME", default=None)}

# User/Auth
AUTH_USER_MODEL = "clients.ClientModel"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework.authentication.TokenAuthentication",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 25,
}

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}

# GRPC
INSECURE_GRPC_HOST = config("INSECURE_GRPC_HOST")
## add TSL CONFIG
