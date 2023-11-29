from __future__ import annotations
from typing import Dict, Any

from imdb import db
from imdb.auth.domain.i_dto import IDto

class Hotel(db.Model, IDto):
    __tablename__ = "hotel"
    number_of_rooms = db.Column(db.Integer)

    object_id = db.Column(db.Integer, db.ForeignKey('object.id'), primary_key=True)

    object = db.relationship("Object", back_populates="hotel", primaryjoin="Object.id == Hotel.object_id ",uselist=False)

    def __repr__(self) -> str:
        return f"Hotel(object_id={self.object_id}, number_of_rooms={self.number_of_rooms})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "object_id": self.object_id,
            "number_of_rooms": self.number_of_rooms,
        }

    @classmethod
    def create_from_data(cls, form_data: Dict[str, Any]) -> Hotel:
        obj = cls(
            object_id=form_data.get("object_id"),
            number_of_rooms=form_data.get("number_of_rooms"),
        )
        return obj
