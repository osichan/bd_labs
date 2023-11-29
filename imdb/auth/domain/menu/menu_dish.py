from __future__ import annotations
from typing import Dict, Any

from imdb import db
from imdb.auth.domain.i_dto import IDto


class MenuDish(db.Model, IDto):
    __tablename__ = "menu_dish"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))

    menu = db.relationship("Menu", back_populates="menu_dish")
    dish = db.relationship("Dish", back_populates="menu_dish")

    def __repr__(self) -> str:
        return f"MenuDish(menu_id={self.menu_id}, dish_id={self.dish_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "menu_id": self.menu_id,
            "dish_id": self.dish_id,
        }

    @classmethod
    def create_from_data(cls, form_data: Dict[str, Any]) -> MenuDish:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = cls(
            id=form_data.get("id"),
            menu_id=form_data.get("menu_id"),
            dish_id=form_data.get("dish_id"),
        )
        return obj
