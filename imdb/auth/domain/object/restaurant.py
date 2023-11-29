from __future__ import annotations
from typing import Dict, Any

from imdb import db
from imdb.auth.domain.i_dto import IDto

class Restaurant(db.Model, IDto):
    __tablename__ = "restaurant"

    object_id = db.Column(db.Integer, db.ForeignKey('object.id'), primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))

    object = db.relationship("Object", back_populates="restaurant", primaryjoin="Object.id == Restaurant.object_id", uselist=False)
    menu = db.relationship("Menu", back_populates="restaurant")

    def __repr__(self) -> str:
        return f"Restaurant(object_id={self.object_id}, menu_id={self.menu_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "object_id": self.object_id,
            "menu_id": self.menu_id,
        }

    @classmethod
    def create_from_data(cls, form_data: Dict[str, Any]) -> Restaurant:
        return cls(
            object_id=form_data.get("object_id"),
            menu_id=form_data.get("menu_id"),
        )
