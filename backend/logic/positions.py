import logging
from fastapi import APIRouter, Depends, Body, HTTPException
from models import Position
from logic.users import get_user
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

router = APIRouter()
# Create = pydantic_model_creator(Position, exclude=('id', 'catalogs', ))
Edit = pydantic_model_creator(Position, exclude=('catalogs', ))
View = pydantic_model_creator(Position, exclude=('catalogs',))


class Create(BaseModel):
    code: str
    price: int
    tag: str
    emoji: str
    name: str


@router.post('/create')
async def create(created: Create = Body(...), user=Depends(get_user)):
    _catalog = await user.catalog
    position = await Position.create(**created.dict())
    await _catalog.positions.add(position)
    return await View.from_tortoise_orm(position)


@router.put('/edit', response_model=View)
async def edit(edited: Edit = Body(...), user=Depends(get_user)):
    position = await user.catalog.get_or_none(edited.id)
    if position is None:
        raise HTTPException(404, 'Not found')
    await position.update_from_dict(edited.dict())
    await position.save()
    return await View.from_queryset(position)


@router.get('/all')
async def get_all(user=Depends(get_user)):
    return await View.from_queryset(user.catalog.all())
