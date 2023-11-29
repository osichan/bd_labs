from imdb.auth.controller.general_controller import GeneralController
from imdb.auth.service import object_service

class ObjectController(GeneralController):
    _service = object_service

    def get_object_info(self, object_id: int):
        """
        Get information for a specific object.
        :param object_id: ID of the object.
        :return: Object information as a dictionary.
        """
        return self._service.get_object_info(object_id)
