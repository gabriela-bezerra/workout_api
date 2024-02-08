from typing import Annotated

from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema


class Category(BaseSchema):
    name: Annotated[
        str, Field(description="Category's name", example="Scale", max_length=10)
    ]
