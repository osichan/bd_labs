from __future__ import annotations
from typing import Dict, Any

from imdb import db
from imdb.auth.domain.i_dto import IDto

class Buyer(db.Model, IDto):
    __tablename__ = "buyer"

    paycard = db.Column(db.String(16))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)

    comments = db.relationship("Comments", back_populates="buyer", primaryjoin="Buyer.person_id == Comments.buyer_person_id")
    person = db.relationship('Person', back_populates='buyer', primaryjoin="Person.id == Buyer.person_id", uselist=False)

    def __repr__(self) -> str:
        return f"Buyer(paycard='{self.paycard}', person_id={self.person_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "paycard": self.paycard,
            "person_id": self.person_id
        }


    @classmethod
    def create_from_data(cls, form_data: Dict[str, Any]) -> Buyer:

        obj = cls(
            paycard=form_data.get("paycard"),
            person_id=form_data.get("person_id")
        )
        return obj


