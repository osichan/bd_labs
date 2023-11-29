from http import HTTPStatus
from flask import abort
from imdb.auth.dao import object_dao
from imdb.auth.service.general_service import GeneralService

class ObjectService(GeneralService):
    _dao = object_dao

    def get_object_info(self, object_id: int):
        obj = self._dao.find_by_id(object_id)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)

        object_info = {
            "id": obj.id,
            "address": obj.address,
            "name": obj.name,
            "rate": obj.rate,
            "type": obj.type,
            "seller_person_id": obj.seller_person_id,
            # Add other relevant fields from the Object model
        }

        return object_info
