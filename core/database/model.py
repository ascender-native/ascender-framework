from tortoise.models import Model as BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from typing_extensions import Self
from tortoise.queryset import QuerySet
from tortoise.contrib.pydantic.base import PydanticModel

class Model(BaseModel):
    def __new__(cls) -> type[PydanticModel]:
        return pydantic_model_creator(super().__new__())
    
    @staticmethod
    def query(self) -> QuerySet[Self]:
        return QuerySet(self)
    
    
    
