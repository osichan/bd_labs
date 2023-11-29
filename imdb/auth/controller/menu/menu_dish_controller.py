from imdb.auth.controller.general_controller import GeneralController
from imdb.auth.service import menu_dish_service

class MenuDishController(GeneralController):
    _service = menu_dish_service

    def get_dishes_for_menu(self, menu_id: int):
        """
        Get dishes for a specific menu.
        :param menu_id: ID of the menu.
        :return: List of dishes as dictionaries.
        """
        return self._service.get_dishes_for_menu(menu_id)
