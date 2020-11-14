from tortoise import Model, Tortoise
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=128, unique=True)
    hashed_password = fields.CharField(max_length=512)
    catalog: fields.ForeignKeyRelation['models.Catalog']

    def __repr__(self):
        return str(self.email)

    class PydanticMeta:
        exclude = ['id', 'hashed_password', 'is_admin']


class Catalog(Model):
    id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField('models.User')
    positions = fields.ManyToManyField('models.Position')
    entry_code = fields.IntField()


class Tag(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32)


class Position(Model):
    id = fields.IntField(pk=True)
    code = fields.CharField(max_length=32)
    price = fields.IntField()
    name = fields.CharField(max_length=64)
    tag = fields.ForeignKeyField('models.Tag')
    emoji = fields.CharField(max_length=8)


class History(Model):
    id = fields.IntField(pk=True)
    time = fields.DatetimeField(auto_now_add=True)
    info = fields.TextField()
    catalog = fields.ForeignKeyField('models.Catalog')


Tortoise.init_models(["models"], "models")
