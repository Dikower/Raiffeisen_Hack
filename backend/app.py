import os
import contextvars
import logging
import uvicorn
import shutil
from pathlib import Path
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from starlette.middleware.cors import CORSMiddleware
from logic import users, catalogs, tags
from settings import PROD_TORTOISE_ORM, TEST_TORTOISE_ORM
from fill_db import fill_roles


app = FastAPI(
    version='0.0.1',
    title='Data App',
    description='API for the Common Data app based on FastAPI',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    users.router,
    prefix='/users',
    tags=['Users']
)

app.include_router(
    catalogs.router,
    prefix='/catalogs',
    tags=['Catalogs']
)

app.include_router(
    tags.router,
    prefix='/tags',
    tags=['Tags']
)


@app.on_event('startup')
async def startup():
    await Tortoise.init(config=TEST_TORTOISE_ORM)
    await Tortoise.generate_schemas(safe=True)
    await fill_roles()

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)
