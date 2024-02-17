from .personal_access_token import PersonalAccessToken
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

import core.support.auth.model as auth_model

class User(auth_model.User):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    email = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=200)

    tokens = fields.ReverseRelation['PersonalAccessToken']

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    @staticmethod
    def form():
        return pydantic_model_creator(User, name=__class__.__name__, exclude_readonly=True)