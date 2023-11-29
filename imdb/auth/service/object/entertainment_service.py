from http import HTTPStatus
from flask import abort
from imdb.auth.dao import entertainment_dao
from imdb.auth.service.general_service import GeneralService


class EntertainmentService(GeneralService):
    _dao = entertainment_dao

    def get_entertainment_info(self, entertainment_id: int):
        entertainment = self._dao.find_by_id(entertainment_id)
        if entertainment is None:
            abort(HTTPStatus.NOT_FOUND)

        entertainment_info = {
            "object_id": entertainment.object_id,
            "type": entertainment.type,
            # Add other relevant fields from the Entertainment model
        }

        return entertainment_info
