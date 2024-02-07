from workout_api.contrib.schemas import BaseSchema
from pydantic import Field, PositiveFloat
from typing import Annotated


class Category(BaseSchema):
    name: Annotated[
        str, Field(description="Category's name", examples="Scale", max_length=10)
    ]
