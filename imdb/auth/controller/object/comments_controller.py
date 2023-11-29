from imdb.auth.controller.general_controller import GeneralController
from imdb.auth.service import comments_service

class CommentsController(GeneralController):
    _service = comments_service

    def get_comments_for_object(self, object_id: int):
        """
        Get comments for a specific object.
        :param object_id: ID of the object.
        :return: Comments as a list of dictionaries.
        """
        return self._service.get_comments_for_object(object_id)
