from fastapi import APIRouter
from models import History
from typing import List
from tortoise.contrib.pydantic import pydantic_model_creator
router = APIRouter()
View = pydantic_model_creator(History)


@router.get('/', response_model=List[View])
async def get_history():
    return await View.from_queryset(History.all())
