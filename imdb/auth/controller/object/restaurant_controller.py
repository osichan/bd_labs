from imdb.auth.controller.general_controller import GeneralController
from imdb.auth.service import restaurant_service

class RestaurantController(GeneralController):
    _service = restaurant_service

    def find_by_ids(self, object_id: int):
        """
        Find an object by its ID and a menu by its ID.
        :param object_id: ID of the object.
        :param menu_id: ID of the menu.
        :return: The found object and menu.
        """
        # Implement the logic for finding by IDs
        # This might involve using methods from the _service attribute or other logic specific to your application
        return self._service.get_restaurant_info(object_id)

    def get_restaurant_info(self, object_id: int):
        """
        Get restaurant information for a given object and menu IDs.
        :param object_id: ID of the object.
        :param menu_id: ID of the menu.
        :return: Restaurant information as a dictionary.
        """
        return self._service.get_restaurant_info(object_id)
