from config.auth import AuthenticatedExhibit, UnauthenticatedExhibit
from config.jwt import decode_jwt_token
from jose import jwt
from starlette.middleware.authentication import AuthCredentials, AuthenticationBackend
from timemanager.models import Exhibit

from fastapi import HTTPException, Request
from fastapi.security.utils import get_authorization_scheme_param


class BackendAuth(AuthenticationBackend):
    async def authenticate(self, request: Request):
        authorization: str = request.headers.get("Authorization")
        scheme, access_token = get_authorization_scheme_param(authorization)

        if not authorization or scheme.lower() != "bearer":
            return (
                AuthCredentials(["unauthenticated"]),
                UnauthenticatedExhibit(),
            )

        try:
            claims = decode_jwt_token(access_token)
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except Exception:
            return (
                AuthCredentials(["unauthenticated"]),
                UnauthenticatedExhibit(),
            )

        exhibit = Exhibit.objects.filter(uuid=claims["exhibit_uuid"]).first()
        if not exhibit or not exhibit.is_active:
            return (
                AuthCredentials(["unauthenticated"]),
                UnauthenticatedExhibit(),
            )

        if exhibit.is_admin:
            return (
                AuthCredentials(["admin", "authenticated"]),
                AuthenticatedExhibit(exhibit),
            )
        else:
            return AuthCredentials(["authenticated"]), AuthenticatedExhibit(exhibit)
