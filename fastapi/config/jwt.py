from datetime import datetime, timedelta
from typing import Dict

from django.conf import settings
from jose import jwt
from timemanager.models import Exhibit


def create_claims(exhibit: Exhibit) -> dict:
    return {
        "exhibit_uuid": str(exhibit.uuid),
        "exp": datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRATION_SECONDS),
    }


def encode_claims_to_jwt_token(claims: dict) -> str:
    return jwt.encode(claims, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decode_jwt_token(token: str) -> dict:
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])


def response_jwt_token(access_token: str) -> Dict[str, str]:
    return {"token_type": "bearer", "access_token": access_token}
