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
from logic import users, positions
from settings import PROD_TORTOISE_ORM, TEST_TORTOISE_ORM
# from fill_db import fill_roles


app = FastAPI(
    version='0.0.1',
    title='SBP-kassa',
    description='API for the SBP-Kassa',
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
    positions.router,
    prefix='/positions',
    tags=['Positions']
)


for path in ['db/test', 'db/prod']:
    Path(path).mkdir(parents=True, exist_ok=True)


@app.on_event('startup')
async def startup():
    await Tortoise.init(config=TEST_TORTOISE_ORM, modules={'models': ['models']})
    await Tortoise.generate_schemas(safe=True)
    # await fill_roles()


@app.on_event('shutdown')
async def shutdown():
    await Tortoise.close_connections()


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, use_colors=True)
