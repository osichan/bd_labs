from http import HTTPStatus
from flask import abort
from imdb.auth.dao import restaurant_dao
from imdb.auth.service.general_service import GeneralService


# Update the method signature in RestaurantService
class RestaurantService(GeneralService):
    _dao = restaurant_dao

    def get_restaurant_info(self, object_id: int):
        restaurant = self._dao.find_by_ids(object_id)
        if restaurant is None:
            abort(HTTPStatus.NOT_FOUND)

        restaurant_info = {
            "object_id": restaurant.object_id,
            "menu_id": restaurant.menu_id,
        }

        return restaurant_info
