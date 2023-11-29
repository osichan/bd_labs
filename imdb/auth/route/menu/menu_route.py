from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from imdb.auth.controller import menu_controller
from imdb.auth.domain.menu.menu import Menu

menu_bp = Blueprint("menus", __name__, url_prefix="/menus/")

@menu_bp.get("")
def get_all_menus() -> Response:
    return make_response(jsonify(menu_controller.find_all()), HTTPStatus.OK)

@menu_bp.get('/<int:menu_id>')
def get_menu(menu_id: int) -> Response:
    return make_response(jsonify(menu_controller.find_by_id(menu_id)), HTTPStatus.OK)

@menu_bp.put('/<int:menu_id>')
def update_menu(menu_id: int) -> Response:
    content = request.form
    menu = Menu.create_from_data(content)
    menu_controller.update(menu_id, menu)
    return make_response("Menu updated", HTTPStatus.OK)

@menu_bp.patch('/<int:menu_id>')
def patch_menu(menu_id: int) -> Response:
    content = request.form
    menu_controller.patch(menu_id, content)
    return make_response("Menu updated", HTTPStatus.OK)

@menu_bp.delete('/<int:menu_id>')
def delete_menu(menu_id: int) -> Response:
    menu_controller.delete(menu_id)
    return make_response("Menu deleted", HTTPStatus.OK)

@menu_bp.post("")
def create_menu() -> Response:
    content = request.form
    menu = Menu.create_from_data(content)
    menu_id = menu_controller.create(menu)
    return make_response(f"Menu created with ID: {menu_id}", HTTPStatus.CREATED)

# Additional routes for specific operations related to Menu can be added here

