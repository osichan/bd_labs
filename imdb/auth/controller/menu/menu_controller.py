from imdb.auth.controller.general_controller import GeneralController
from imdb.auth.service import menu_service

class MenuController(GeneralController):
    _service = menu_service

    def get_menu_info(self, menu_id: int):
        """
        Get information for a specific menu.
        :param menu_id: ID of the menu.
        :return: Menu information as a dictionary.
        """
        return self._service.get_menu_info(menu_id)
