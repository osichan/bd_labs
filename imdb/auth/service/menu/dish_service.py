from http import HTTPStatus
from flask import abort
from imdb.auth.dao import dish_dao
from imdb.auth.service.general_service import GeneralService


class DishService(GeneralService):
    _dao = dish_dao

    def get_dish_info(self, dish_id: int):
        dish = self._dao.find_by_id(dish_id)
        if dish is None:
            abort(HTTPStatus.NOT_FOUND)

        dish_info = {
            "id": dish.id,
            "name": dish.name,
            "ingredients": dish.ingredients,
            # Add other relevant fields from the Dish model
        }

        return dish_info
