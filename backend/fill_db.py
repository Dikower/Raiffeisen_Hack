from models import Tag


async def fill_roles():
    for name in ['Напитки', 'Закуски', 'Салаты']:
        await Tag.create(name=name)
