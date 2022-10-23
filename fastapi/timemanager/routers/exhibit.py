from timemanager.api import ExhibitAPI
from timemanager.dependencies.auth import login_required
from timemanager.models import Exhibit
from timemanager.schemas import ReadExhibitSchema, UpdateExhibitSchema

from fastapi import APIRouter, Depends, Request

exhibit_router = APIRouter()


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
