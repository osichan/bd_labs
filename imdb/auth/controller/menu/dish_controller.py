from imdb.auth.controller.general_controller import GeneralController
from imdb.auth.service import dish_service

class DishController(GeneralController):
    _service = dish_service

    def get_dish_info(self, dish_id: int):
        """
        Get information for a specific dish.
        :param dish_id: ID of the dish.
        :return: Dish information as a dictionary.
        """
        return self._service.get_dish_info(dish_id)
