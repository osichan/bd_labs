from http import HTTPStatus
from flask import abort
from imdb.auth.dao import hotel_dao
from imdb.auth.service.general_service import GeneralService


class HotelService(GeneralService):
    _dao = hotel_dao

    def get_hotel_info(self, hotel_id: int):
        hotel = self._dao.find_by_id(hotel_id)
        if hotel is None:
            abort(HTTPStatus.NOT_FOUND)

        hotel_info = {
            "object_id": hotel.object_id,
            "number_of_rooms": hotel.number_of_rooms,
            # Add other relevant fields from the Hotel model
        }

        return hotel_info
