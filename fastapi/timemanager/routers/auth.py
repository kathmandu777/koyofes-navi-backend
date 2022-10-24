from fastapi import APIRouter, Depends, Request

from ..api import AuthAPI
from ..schemas import LoginSchema, Token

auth_router = APIRouter()


@auth_router.post("/login", response_model=Token)
async def login(request: Request, schema: LoginSchema = Depends()) -> dict[str, str]:
    return AuthAPI.login(request, schema)
