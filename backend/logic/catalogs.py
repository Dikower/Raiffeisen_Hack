from tortoise.contrib.pydantic import pydantic_model_creator
from fastapi import APIRouter, HTTPException, Body, Depends
from logic.users import get_user
from models import Catalog
from typing import List
from pydantic import BaseModel

router = APIRouter()
View = pydantic_model_creator(Catalog)


@router.get('/{entry_code}', response_model=View)
async def get_catalog(entry_code: int):
    catalog = await Catalog.get_or_none(entry_code=entry_code)
    if not catalog:
        raise HTTPException(404, 'Catalog not found')
    return await View.from_tortoise_orm(catalog)
