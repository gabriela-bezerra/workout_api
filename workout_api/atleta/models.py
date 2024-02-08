from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel


class AthleteModel(BaseModel):
    __tablename__ = "athletes"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    hight: Mapped[float] = mapped_column(Float, nullable=False)
    sex: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    category: Mapped["CategoryModel"] = relationship(
        back_populates="athlete", lazy="selectin"
    )
    category_id = Mapped[int] = mapped_column(ForeignKey("categories.pk_id"))
    trainning_center: Mapped["TrainningCenterModel"] = relationship(
        back_populates="athlete", lazy="selectin"
    )
    trainning_center_id = Mapped[int] = mapped_column(
        ForeignKey("trainning_centers.pk_id")
    )
