from __future__ import annotations
from typing import Dict, Any

from imdb import db
from imdb.auth.domain.i_dto import IDto

class Seller(db.Model, IDto):
    __tablename__ = "seller"

    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)

    person = db.relationship('Person', back_populates='seller', primaryjoin="Person.id == Seller.person_id", uselist=False)
    object = db.relationship('Object', back_populates='seller')

    def __repr__(self) -> str:
        return f"Seller(person_id={self.person_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object_dao.py into DTO without relationship
        :return: DTO object_dao.py as dictionary
        """
        return {
            "person_id": self.person_id,
        }

    @classmethod
    def create_from_data(cls,form_data: Dict[str, Any]) -> Seller:
        """
        Creates domain object_dao.py from DTO
        :param dto_dict: DTO object_dao.py
        :return: Domain object_dao.py
        """

        obj = Seller(
            person_id=form_data.get("person_id")
        )
        return obj