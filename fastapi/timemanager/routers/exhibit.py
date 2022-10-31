from config.dependencies.auth import login_required

from fastapi import APIRouter, Depends, Request

from ..api import ExhibitAPI
from ..models import Exhibit
from ..schemas import ReadExhibitSchema, UpdateExhibitSchema

exhibit_router = APIRouter()
exhibits_router = APIRouter()


@exhibits_router.get("/", response_model=list[ReadExhibitSchema])
async def gets(request: Request) -> list[Exhibit]:
    return ExhibitAPI.gets(request)


@exhibit_router.get(
    "/", response_model=ReadExhibitSchema, dependencies=[Depends(login_required)]
)
async def get(request: Request) -> Exhibit:
    return ExhibitAPI.get(request)


@exhibit_router.put(
    "/",
    response_model=ReadExhibitSchema,
    dependencies=[Depends(login_required)],
)
async def update(request: Request, schema: UpdateExhibitSchema) -> Exhibit:
    return ExhibitAPI.update(request, schema)
