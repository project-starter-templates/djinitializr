from config.env import BASE_DIR, env
from config.settings.base import *  # noqa: F403
from config.settings.base import INSTALLED_APPS, MIDDLEWARE

# DEBUG MODE
DEBUG = env.bool(var="DJANGO_DEBUG", default=True)

# Application development settings
DEVELOP_APPS = []
INSTALLED_APPS.extend(DEVELOP_APPS)

# Middleware development settings
DEVELOP_MIDDLEWARE = []
MIDDLEWARE.extend(DEVELOP_MIDDLEWARE)


# Database development settings
if env.bool(var="DB_CONNECTION", default="sqlite") != "sqlite":
    DATABASES = {
        "default": {
            "ENGINE": env.str(var="DB_ENGINE"),
            "NAME": env.str(var="DB_NAME"),
            "USER": env.str(var="DB_USER"),
            "PASSWORD": env.str(var="DB_PASSWORD"),
            "HOST": env.str(var="DB_HOST"),
            "PORT": env.int(var="DB_PORT"),
        }
    }


# Cache development settings
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}


# Email settings
EMAIL_HOST = env("EMAIL_HOST", default="mailpit")
EMAIL_PORT = 1025


# Storages development settings
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Media files
MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = BASE_DIR / "mediafiles"
