from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from imdb.auth.controller import menu_dish_controller
from imdb.auth.domain.menu.menu_dish import MenuDish

menu_dish_bp = Blueprint("menu_dishes", __name__, url_prefix="/menu-dishes/")

@menu_dish_bp.get("/")
def get_all_menu_dishes() -> Response:
    return make_response(jsonify(menu_dish_controller.find_all()), HTTPStatus.OK)


@menu_dish_bp.get('/<int:menu_id>')
def get_menu_dish(menu_id: int) -> Response:
    return make_response(jsonify(menu_dish_controller.find_by_id(menu_id)), HTTPStatus.OK)

@menu_dish_bp.put('/<int:menu_id>')
def update_menu_dish(menu_id: int) -> Response:
    content = request.form
    menu_dish = MenuDish.create_from_data(content)
    menu_dish_controller.update(menu_id, menu_dish)
    return make_response("MenuDish updated", HTTPStatus.OK)

@menu_dish_bp.patch('/<int:menu_id>')
def patch_menu_dish(menu_id: int) -> Response:
    content = request.form
    menu_dish_controller.patch(menu_id, content)
    return make_response("MenuDish updated", HTTPStatus.OK)

@menu_dish_bp.delete('/<int:menu_id>')
def delete_menu_dish(menu_id: int) -> Response:
    menu_dish_controller.delete(menu_id)
    return make_response("MenuDish deleted", HTTPStatus.OK)

@menu_dish_bp.post("")
def create_menu_dish() -> Response:
    content = request.form
    menu_dish = MenuDish.create_from_dto(content)
    menu_dish_controller.create(menu_dish)
    return make_response("MenuDish created", HTTPStatus.CREATED)