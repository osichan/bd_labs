from http import HTTPStatus
from flask import abort
from imdb.auth.dao import menu_dish_dao
from imdb.auth.service.general_service import GeneralService


class MenuDishService(GeneralService):
    _dao = menu_dish_dao

    def get_menu_dish_info(self, menu_id: int):
        menu_dish = self._dao.find_by_id(menu_id)
        if menu_dish is None:
            abort(HTTPStatus.NOT_FOUND)

        menu_dish_info = {
            "menu_id": menu_dish.menu_id,
            "dish_id": menu_dish.dish_id,
            # Add other relevant fields from the MenuDish model
        }

        return menu_dish_info
