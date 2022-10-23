from config.jwt import create_claims, encode_claims_to_jwt_token, response_jwt_token
from config.password import verify_password
from timemanager.models import Exhibit
from timemanager.schemas.auth import LoginSchema

from fastapi import HTTPException, Request


class AuthAPI:
    @classmethod
    def login(cls, request: Request, schema: LoginSchema) -> dict[str, str]:
        credentials = {"name": schema.name, "password": schema.password}

        if all(credentials.values()):
            exhibit = cls._authenticate_exhibit(**credentials)
            claims = create_claims(exhibit)
        else:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        return response_jwt_token(encode_claims_to_jwt_token(claims))

    @classmethod
    def _authenticate_exhibit(cls, name: str, password: str) -> Exhibit:
        exhibit = Exhibit.objects.filter(name=name).first()

        if not exhibit:
            raise HTTPException(status_code=400, detail="No such exhibit")
        if not verify_password(password, exhibit.password) or not exhibit.is_active:
            raise HTTPException(status_code=400, detail="Invalid password")
        return exhibit
