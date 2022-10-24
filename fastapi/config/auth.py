from starlette import authentication
from timemanager.models import Exhibit

from fastapi import HTTPException, Request, security


class OAuth2PasswordBearer(security.OAuth2PasswordBearer):
    """OAuth2PasswordBearerのラッパー."""

    async def __call__(self, request: Request) -> str | None:
        authorization: str = request.headers.get("Authorization")
        scheme, param = security.utils.get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(status_code=400, detail="Invalid token")
            else:
                return None
        return param


class AuthenticatedExhibit(authentication.SimpleUser):
    def __init__(self, exhibit: Exhibit) -> None:
        self.exhibit = exhibit


class UnauthenticatedExhibit(authentication.UnauthenticatedUser):
    pass
