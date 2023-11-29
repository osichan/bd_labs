from http import HTTPStatus
from flask import abort
from imdb.auth.dao import menu_dao
from imdb.auth.service.general_service import GeneralService


class MenuService(GeneralService):
    _dao = menu_dao

    def get_menu_info(self, menu_id: int):
        menu = self._dao.find_by_id(menu_id)
        if menu is None:
            abort(HTTPStatus.NOT_FOUND)

        menu_info = {
            "id": menu.id,
            "description": menu.description,
            # Add other relevant fields from the Menu model
        }

        return menu_info
