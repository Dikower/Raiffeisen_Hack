from fastapi import APIRouter, HTTPException
from models import History, Catalog
from typing import List
from tortoise.contrib.pydantic import pydantic_model_creator
router = APIRouter()
View = pydantic_model_creator(History, exclude=('catalog', ))


@router.get('/', response_model=List[View])
async def get_history():
    return await View.from_queryset(History.all())


@router.get('/{entry_code}/last', response_model=View)
async def get_last(entry_code: str):
    catalog = await Catalog.get_or_none(entry_code=entry_code)
    if not catalog:
        raise HTTPException(404, 'Catalog not found')
    filtered = await History.filter(catalog=catalog)
    if len(filtered) == 0:
        return {}
    return await View.from_tortoise_orm(filtered[-1])
