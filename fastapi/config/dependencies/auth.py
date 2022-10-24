from config.auth import OAuth2PasswordBearer

from fastapi import Depends, HTTPException, Request

PASSWORD_LOGIN = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def login_required(
    request: Request, password_login=Depends(PASSWORD_LOGIN)
) -> None:
    if not request.user.is_authenticated:
        raise HTTPException(status_code=401, detail="Not authenticated")


async def admin_required(
    request: Request, password_login=Depends(PASSWORD_LOGIN)
) -> None:
    if not request.user.is_authenticated:
        raise HTTPException(status_code=401, detail="Not authenticated")
    if not request.user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")
