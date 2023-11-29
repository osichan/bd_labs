from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from imdb.auth.controller import dish_controller
from imdb.auth.domain.menu.dish import Dish

dish_bp = Blueprint("dishes", __name__, url_prefix="/dishes/")

@dish_bp.get("")
def get_all_dishes() -> Response:
    return make_response(jsonify(dish_controller.find_all()), HTTPStatus.OK)

@dish_bp.get('/<int:dish_id>')
def get_dish(dish_id: int) -> Response:
    return make_response(jsonify(dish_controller.find_by_id(dish_id)), HTTPStatus.OK)

@dish_bp.put('/<int:dish_id>')
def update_dish(dish_id: int) -> Response:
    content = request.form
    dish = Dish.create_from_data(content)
    dish_controller.update(dish_id, dish)
    return make_response("Dish updated", HTTPStatus.OK)

@dish_bp.patch('/<int:dish_id>')
def patch_dish(dish_id: int) -> Response:
    content = request.form
    dish_controller.patch(dish_id, content)
    return make_response("Dish updated", HTTPStatus.OK)

@dish_bp.delete('/<int:dish_id>')
def delete_dish(dish_id: int) -> Response:
    dish_controller.delete(dish_id)
    return make_response("Dish deleted", HTTPStatus.OK)

@dish_bp.post("")
def create_dish() -> Response:
    content = request.form
    dish = Dish.create_from_data(content)
    dish_id = dish_controller.create(dish)
    return make_response(f"Dish created with ID: {dish_id}", HTTPStatus.CREATED)

# Additional routes for specific operations related to Dish can be added here

