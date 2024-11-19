from config.env import env
from config.settings.base import *  # noqa: F403

# DEBUG MODE
DEBUG = env.bool(var="DJANGO_DEBUG", default=False)


# Database settings
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

# Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env.str(var="REDIS_URL", default="redis://localhost:6379/0"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}


# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


# Storages production settings (whitenoise)
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}
