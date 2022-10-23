"""ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

envstate = os.getenv("ENV_STATE", "production")
if envstate == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
elif envstate == "staging":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.staging")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")


application = get_asgi_application()


"""
FastAPI settings
"""
import logging
import logging.config
from datetime import datetime

from pytz import timezone
from starlette.middleware.authentication import AuthenticationMiddleware
from timemanager.middlewares.auth import BackendAuth
from timemanager.routers import auth_router, exhibit_router

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .log import LOGGING

fastapp = FastAPI()


def tokyo_time(*args):
    return datetime.now(timezone("Asia/Tokyo")).timetuple()


logging.Formatter.converter = tokyo_time
logging.config.dictConfig(LOGGING)

# middlewares (後に追加したものが先に実行される)
fastapp.add_middleware(AuthenticationMiddleware, backend=BackendAuth())

fastapp.include_router(exhibit_router, tags=["exhibits"], prefix="/exhibit")
fastapp.include_router(auth_router, tags=["auth"], prefix="/auth")

# to mount Django
fastapp.mount("/django", application)
fastapp.mount("/static", StaticFiles(directory="static"), name="static")
fastapp.mount("/media", StaticFiles(directory="media"), name="media")
