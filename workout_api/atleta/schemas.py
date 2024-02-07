from pydantic import Field, PositiveFloat
from typing import Annotated
from workout_api.contrib.schemas import BaseSchema


class Athlete(BaseSchema):
    name: Annotated[
        str, Field(description="Athlete's name", examples="Paul", max_length=50)
    ]
    phone_number: Annotated[
        str,
        Field(
            description="Athlete's phone number", examples="2068614012", max_length=10
        ),
    ]
    age: Annotated[int, Field(description="Athlete's age", examples="20")]
    weight: Annotated[
        PositiveFloat, Field(description="Athlete's weight", examples="135")
    ]
    height: Annotated[
        PositiveFloat, Field(description="Athlete's height", examples="162")
    ]
    sex: Annotated[str, Field(description="Athlete's sex", examples="M", max_length=1)]
