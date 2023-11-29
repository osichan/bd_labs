# menu_dao.py
from __future__ import annotations
from typing import Dict, Any

from imdb import db
from imdb.auth.domain.i_dto import IDto

class Menu(db.Model, IDto):
    __tablename__ = "menu"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(70))

    menu_dish = db.relationship("MenuDish", back_populates="menu")
    restaurant = db.relationship("Restaurant", back_populates="menu")

    def __repr__(self) -> str:
        return f"Menu(id={self.id}, description='{self.description}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "description": self.description,
        }

    @classmethod
    def create_from_data(cls, form_data: Dict[str, Any]) -> Menu:
        return cls(
            description=form_data.get("description"),
        )
