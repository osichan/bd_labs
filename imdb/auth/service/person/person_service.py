from http import HTTPStatus
from flask import abort
from imdb.auth.dao import person_dao
from imdb.auth.service.general_service import GeneralService


class PersonService(GeneralService):
    _dao = person_dao

    def get_buyer_info(self, person_id: int):
        person = self._dao.find_by_id(person_id)
        if person is None:
            abort(HTTPStatus.NOT_FOUND)

        buyer_info = {"buyer": None}
        if person.buyer:
            buyer_info["buyer"] = {
                "buyer_id": person.buyer.id,
                "additional_info": person.buyer.additional_info  # Add other relevant fields from the Buyer model
            }

        return buyer_info

    def get_seller_info(self, person_id: int):
        person = self._dao.find_by_id(person_id)
        if person is None:
            abort(HTTPStatus.NOT_FOUND)

        seller_info = {"seller": None}
        if person.seller:
            seller_info["seller"] = {
                "seller_id": person.seller.id,
                "additional_info": person.seller.additional_info  # Add other relevant fields from the Seller model
            }

        return seller_info
