# dish_dao.py
from __future__ import annotations
from typing import Dict, Any

from imdb import db
from imdb.auth.domain.i_dto import IDto

class Dish(db.Model, IDto):
    __tablename__ = "dish"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    ingredients = db.Column(db.String(700))


    menu_dish = db.relationship("MenuDish", back_populates="dish")


    def __repr__(self) -> str:
        return f"Dish(id={self.id}, name='{self.name}', ingredients='{self.ingredients}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients,
        }

    @classmethod
    def create_from_data(cls, form_data: Dict[str, Any]) -> Dish:
        return cls(
            name=form_data.get("name"),
            ingredients=form_data.get("ingredients"),
        )

