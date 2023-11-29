from __future__ import annotations
from typing import Dict, Any

from imdb import db
from imdb.auth.domain.i_dto import IDto

class Person(db.Model, IDto):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45))
    second_name = db.Column(db.String(45))
    email = db.Column(db.String(45))

    buyer = db.relationship("Buyer", back_populates="person", primaryjoin="Person.id == Buyer.person_id", uselist=False)
    seller = db.relationship("Seller", back_populates="person", primaryjoin="Person.id == Seller.person_id", uselist=False)

    def __repr__(self) -> str:
        return f"Person(id={self.id}, first_name='{self.first_name}', second_name='{self.second_name}', email='{self.email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "second_name": self.second_name,
            "email": self.email
        }

    @classmethod
    def create_from_data(cls, form_data: Dict[str, Any]) -> Person:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        print(form_data)
        obj = cls(
            first_name=form_data.get("first_name"),
            second_name=form_data.get("second_name"),
            email=form_data.get("email")
        )
        return obj
