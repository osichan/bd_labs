from __future__ import annotations
from typing import Dict, Any

from imdb import db
from imdb.auth.domain.i_dto import IDto

class Object(db.Model, IDto):
    __tablename__ = "object"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(45))
    name = db.Column(db.String(45))
    rate = db.Column(db.Integer)
    type = db.Column(db.String(45))

    seller_person_id = db.Column(db.Integer, db.ForeignKey('seller.person_id'))

    # Specify foreign key names explicitly
    seller = db.relationship('Seller', back_populates="object", foreign_keys=[seller_person_id])
    comments = db.relationship("Comments", back_populates="object", primaryjoin="Object.id == Comments.object_id")
    hotel = db.relationship("Hotel", back_populates="object", primaryjoin="Object.id == Hotel.object_id",
                            uselist=False)
    entertainment = db.relationship("Entertainment", back_populates="object",
                                    primaryjoin="Object.id == Entertainment.object_id", uselist=False)
    restaurant = db.relationship("Restaurant", back_populates="object",
                                primaryjoin="Object.id == Restaurant.object_id", uselist=False)

    def __repr__(self) -> str:
        return f"Object(" \
               f"id={self.id}, " \
               f"address='{self.address}', " \
               f"name='{self.name}', " \
               f"rate={self.rate}, " \
               f"type='{self.type}', " \
               f"seller_person_id={self.seller_person_id}" \
               f")"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "address": self.address,
            "name": self.name,
            "rate": self.rate,
            "type": self.type,
            "seller_person_id": self.seller_person_id
        }

    @classmethod
    def create_from_data(cls, form_data: Dict[str, Any]) -> Object:
        obj = cls(
            id=form_data.get("id"),
            address=form_data.get("address"),
            name=form_data.get("name"),
            rate=form_data.get("rate"),
            type=form_data.get("type"),
            seller_person_id=form_data.get("seller_person_id")
        )
        return obj
