"""ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

"""
Settings
"""
env_state = os.getenv("ENV_STATE", "production")
if env_state == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
elif env_state == "staging":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.staging")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")


"""
Logging
"""
import logging
import logging.config
from datetime import datetime

from pytz import timezone

from .log import LOGGING


def tokyo_time(*args):  # type: ignore
    return datetime.now(timezone("Asia/Tokyo")).timetuple()


logging.Formatter.converter = tokyo_time
logging.config.dictConfig(LOGGING)


"""
Django settings
"""
application = get_asgi_application()


"""
Fast API settings
"""
from bingo.routers import prize_router
from config.middlewares.auth import BackendAuth
from starlette.middleware.authentication import AuthenticationMiddleware
from timemanager.routers import auth_router, exhibit_router, waiting_time_router

from fastapi import FastAPI

fastapp = FastAPI()

# middlewares (後に追加したものが先に実行される)
fastapp.add_middleware(AuthenticationMiddleware, backend=BackendAuth())

# routers
fastapp.include_router(exhibit_router, tags=["展示"], prefix="/exhibit")
fastapp.include_router(auth_router, tags=["auth"], prefix="/auth")
fastapp.include_router(waiting_time_router, tags=["待ち時間"], prefix="/waiting-time")
fastapp.include_router(prize_router, tags=["BINGO景品"], prefix="/prize")

# to mount Django
# fastapp.mount("/django", application)
# fastapp.mount("/static", StaticFiles(directory="static"), name="static")
# fastapp.mount("/media", StaticFiles(directory="media"), name="media")
