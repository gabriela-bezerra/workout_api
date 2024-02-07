from workout_api.atleta.models import AthleteModel
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String


class CategoryModel(BaseModel):
    __tablename__ = "categories"
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    category: Mapped["AthleteModel"] = relationship(back_populates="category")
