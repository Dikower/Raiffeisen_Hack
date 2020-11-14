from tortoise.contrib.pydantic import pydantic_model_creator
from fastapi import APIRouter, HTTPException
from models import Catalog

router = APIRouter()
View = pydantic_model_creator(Catalog)


@router.get('/{entry_code}/catalog', response_model=View)
async def get_catalog(entry_code: int):
    catalog = await Catalog.get_or_none(entry_code=entry_code)
    if not catalog:
        raise HTTPException(404, 'Catalog not found')
    print(await catalog.positions.all())
    return await View.from_queryset(catalog.positions.all())
