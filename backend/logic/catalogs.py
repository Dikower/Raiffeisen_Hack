from tortoise.contrib.pydantic import pydantic_model_creator
from fastapi import APIRouter, HTTPException, Body, Depends
from logic.users import get_user
from models import Catalog
from typing import List
from pydantic import BaseModel

router = APIRouter()
View = pydantic_model_creator(Catalog)


class Delete(BaseModel):
    ids: List[int]


@router.get('/{entry_code}/catalog', response_model=View)
async def get_catalog(entry_code: int):
    catalog = await Catalog.get_or_none(entry_code=entry_code)
    if not catalog:
        raise HTTPException(404, 'Catalog not found')
    return await View.from_tortoise_orm(catalog)


@router.delete('/delete_positions', response_model=View)
async def edit_catalog(to_delete: Delete = Body(...), user=Depends(get_user)):
    catalog = await user.catalog
    for _id in to_delete.dict()['ids']:
        position = await catalog.positions.filter(id=_id)
        if position:
            position = position[0]
            await position.delete()
    catalog = await user.catalog
    return await View.from_tortoise_orm(catalog)
