from __future__ import annotations
from typing import Dict, Any

from imdb import db
from imdb.auth.domain.i_dto import IDto

class Comments(db.Model, IDto):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(255))

    object_id = db.Column(db.Integer, db.ForeignKey('object.id'))
    buyer_person_id = db.Column(db.Integer, db.ForeignKey('buyer.person_id'))

    # Define relationships with explicit primary joins
    object = db.relationship("Object", back_populates="comments")
    buyer = db.relationship("Buyer", back_populates="comments")

    def __repr__(self) -> str:
        return f"Comments(id={self.id}, object_id={self.object_id}, buyer_person_id={self.buyer_person_id}, comment='{self.comment}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "object_id": self.object_id,
            "buyer_person_id": self.buyer_person_id,
            "comment": self.comment
        }

    @classmethod
    def create_from_data(cls,form_data: Dict[str, Any]) -> Comments:
        obj = cls(
            id=form_data.get("id"),
            object_id=form_data.get("object_id"),
            buyer_person_id=form_data.get("buyer_person_id"),
            comment=form_data.get("comment")
        )
        return obj
