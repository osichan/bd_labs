from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from imdb.auth.controller import restaurant_controller
from imdb.auth.domain.object.restaurant import Restaurant

restaurant_bp = Blueprint("restaurants", __name__, url_prefix="/restaurants/")

@restaurant_bp.get("")
def get_all_restaurants() -> Response:
    return make_response(jsonify(restaurant_controller.find_all()), HTTPStatus.OK)

@restaurant_bp.get('/<int:object_id>')
def get_restaurant(object_id: int) -> Response:
    restaurant = Restaurant.query.filter_by(object_id=object_id).first()

    if restaurant:
        person_info = restaurant.object.put_into_dto()
        restaurant_info = restaurant.put_into_dto()
        combined_info = {**person_info, **restaurant_info}
        return jsonify(combined_info), 200
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@restaurant_bp.put('/<int:object_id>')
def update_restaurant(object_id: int) -> Response:
    content = request.form
    restaurant = Restaurant.create_from_data(content)
    restaurant_controller.update(object_id, restaurant)
    return make_response("Restaurant updated", HTTPStatus.OK)

@restaurant_bp.patch('/<int:object_id>')
def patch_restaurant(object_id: int) -> Response:
    content = request.form
    restaurant_controller.patch(object_id, content)
    return make_response("Restaurant updated", HTTPStatus.OK)

@restaurant_bp.delete('/<int:object_id>')
def delete_restaurant(object_id: int) -> Response:
    restaurant_controller.delete(object_id)
    return make_response("Restaurant deleted", HTTPStatus.OK)

@restaurant_bp.post("")
def create_restaurant() -> Response:
    content = request.form
    restaurant = Restaurant.create_from_data(content)
    restaurant_controller.create(restaurant)
    return make_response("Restaurant created", HTTPStatus.CREATED)

# Additional routes for specific operations related to Restaurant can be added here

