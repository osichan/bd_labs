from imdb.auth.controller.general_controller import GeneralController
from imdb.auth.service import entertainment_service

class EntertainmentController(GeneralController):
    _service = entertainment_service

    def get_entertainment_info_for_object(self, object_id: int):
        """
        Get entertainment information for a specific object.
        :param object_id: ID of the object.
        :return: Entertainment information as a dictionary.
        """
        return self._service.get_entertainment_info_for_object(object_id)
