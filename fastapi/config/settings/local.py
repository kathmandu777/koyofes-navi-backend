import os

from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql_psycopg2"),
        "NAME": os.getenv("DB_NAME", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.getenv("DB_USER", "user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "password"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
