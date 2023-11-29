from http import HTTPStatus
from flask import abort
from imdb.auth.dao import buyer_dao
from imdb.auth.service.general_service import GeneralService


class BuyerService(GeneralService):
    _dao = buyer_dao

    def get_buyer_by_person_id(self, person_id: int):
        buyer = self._dao.find_by_person_id(person_id)
        if buyer is None:
            abort(HTTPStatus.NOT_FOUND)

        buyer_info = {
            "paycard": buyer.paycard,
            "person_id": buyer.person_id,
            # Add other relevant fields from the Buyer model
        }

        return buyer_info
