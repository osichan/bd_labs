from http import HTTPStatus
from flask import abort
from imdb.auth.dao import seller_dao
from imdb.auth.service.general_service import GeneralService


class SellerService(GeneralService):
    _dao = seller_dao

    def get_seller_by_person_id(self, person_id: int):
        seller = self._dao.find_by_person_id(person_id)
        if seller is None:
            abort(HTTPStatus.NOT_FOUND)

        seller_info = {
            "person_id": seller.person_id,
            "object_count": len(seller.object) if seller.object else 0,
            # Add other relevant fields from the Seller model
        }

        return seller_info
