from imdb.auth.controller.general_controller import GeneralController
from imdb.auth.service import hotel_service

class HotelController(GeneralController):
    _service = hotel_service

    def get_hotel_info_for_object(self, object_id: int):
        """
        Get hotel information for a specific object.
        :param object_id: ID of the object.
        :return: Hotel information as a dictionary.
        """
        return self._service.get_hotel_info_for_object(object_id)
