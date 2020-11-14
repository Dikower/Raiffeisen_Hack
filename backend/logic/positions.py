import logging
from fastapi import APIRouter, Depends, Body, HTTPException, Path
from models import Position
from logic.users import get_user
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

router = APIRouter()
Edit = pydantic_model_creator(Position, exclude=('catalog', ))
View = pydantic_model_creator(Position, exclude=('catalog',))


class Create(BaseModel):
    code: str
    price: int
    name: str
    tag: str
    emoji: str


@router.post('/create', response_model=View)
async def create(created: Create = Body(...), user=Depends(get_user)):
    _catalog = await user.catalog
    position = await Position.create(**created.dict())
    await _catalog.positions.add(position)
    return await View.from_tortoise_orm(position)


@router.put('/edit', response_model=View)
async def edit(edited: Edit = Body(...), user=Depends(get_user)):
    _catalog = await user.catalog
    position = await _catalog.positions.filter(id=edited.id)
    if not position:
        raise HTTPException(404, 'Not found')
    edited = edited.dict()
    position = position[0]
    del edited['id']
    await position.update_from_dict(edited)
    await position.save()
    return await View.from_tortoise_orm(position)


@router.get('/all')
async def get_all(user=Depends(get_user)):
    _catalog = await user.catalog
    return await View.from_queryset(_catalog.positions.all())
