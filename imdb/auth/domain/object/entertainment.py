from __future__ import annotations
from typing import Dict, Any

from imdb import db
from imdb.auth.domain.i_dto import IDto

class Entertainment(db.Model, IDto):
    __tablename__ = "entertainment"
    type = db.Column(db.String(45))

    object_id = db.Column(db.Integer, db.ForeignKey('object.id'), primary_key=True)

    object = db.relationship("Object", back_populates="entertainment",
                             primaryjoin="Object.id == Entertainment.object_id ",uselist=False)

    def __repr__(self) -> str:
        return f"Entertainment(object_id={self.object_id}, type={self.type})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "object_id": self.object_id,
            "type": self.type,
        }

    @classmethod
    def create_from_data(cls, form_data: Dict[str, Any]) -> Entertainment:
        obj = cls(
            object_id=form_data.get("object_id"),
            type=form_data.get("type"),
        )
        return obj
