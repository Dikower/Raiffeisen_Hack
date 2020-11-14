from tortoise import Model, Tortoise
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=128, unique=True)
    hashed_password = fields.CharField(max_length=512)

    catalog: fields.ReverseRelation['Catalog']

    class PydanticMeta:
        exclude = ['hashed_password', ]


class Catalog(Model):
    id = fields.IntField(pk=True)
    entry_code = fields.CharField(max_length=6)
    user = fields.OneToOneField('models.User', related_name='catalog')
    positions = fields.ManyToManyField('models.Position', related_name='catalog')

    class PydanticMeta:
        exclude = ['historys', ]


class Position(Model):
    id = fields.IntField(pk=True)
    code = fields.CharField(max_length=32)
    price = fields.IntField()
    name = fields.CharField(max_length=64)
    tag = fields.CharField(max_length=32)
    emoji = fields.CharField(max_length=8)

    catalog: fields.ManyToManyRelation['Catalog']

    class PydanticMeta:
        exclude = ['historys']


class History(Model):
    id = fields.IntField(pk=True)
    time = fields.DatetimeField(auto_now_add=True)
    info = fields.TextField()


Tortoise.init_models(["models"], "models")
