from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from imdb.auth.controller import hotel_controller
from imdb.auth.domain.object.hotel import Hotel

hotel_bp = Blueprint("hotels", __name__, url_prefix="/hotels/")

@hotel_bp.get("")
def get_all_hotels() -> Response:
    return make_response(jsonify(hotel_controller.find_all()), HTTPStatus.OK)

@hotel_bp.get('/<int:object_id>')
def get_hotel(object_id: int) -> Response:
    hotel = Hotel.query.filter_by(object_id=object_id).first()

    if hotel:
        person_info = hotel.object.put_into_dto()
        hotel_info = hotel.put_into_dto()
        combined_info = {**person_info, **hotel_info}
        return jsonify(combined_info), 200
    else:
        return jsonify({"error": "Hotel not found"}), 404

@hotel_bp.put('/<int:object_id>')
def update_hotel(object_id: int) -> Response:
    content = request.form
    hotel = Hotel.create_from_data(content)
    hotel_controller.update(object_id, hotel)
    return make_response("Hotel updated", HTTPStatus.OK)

@hotel_bp.patch('/<int:object_id>')
def patch_hotel(object_id: int) -> Response:
    content = request.form
    hotel_controller.patch(object_id, content)
    return make_response("Hotel updated", HTTPStatus.OK)

@hotel_bp.delete('/<int:object_id>')
def delete_hotel(object_id: int) -> Response:
    hotel_controller.delete(object_id)
    return make_response("Hotel deleted", HTTPStatus.OK)

@hotel_bp.post("")
def create_hotel() -> Response:
    content = request.form
    hotel = Hotel.create_from_data(content)
    hotel_controller.create(hotel)
    return make_response("Hotel created", HTTPStatus.CREATED)

# Additional routes for specific operations related to Hotel can be added here

