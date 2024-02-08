from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema


class Athlete(BaseSchema):
    name: Annotated[
        str, Field(description="Athlete's name", example="Paul", max_length=50)
    ]
    phone_number: Annotated[
        str,
        Field(
            description="Athlete's phone number", example="2068614012", max_length=10
        ),
    ]
    age: Annotated[int, Field(description="Athlete's age", example="20")]
    weight: Annotated[
        PositiveFloat, Field(description="Athlete's weight", example="135")
    ]
    height: Annotated[
        PositiveFloat, Field(description="Athlete's height", example="162")
    ]
    sex: Annotated[str, Field(description="Athlete's sex", example="M", max_length=1)]
