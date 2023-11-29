from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from imdb.auth.controller import entertainment_controller
from imdb.auth.domain.object.entertainment import Entertainment

entertainment_bp = Blueprint("entertainments", __name__, url_prefix="/entertainments/")

@entertainment_bp.get("")
def get_all_entertainments() -> Response:
    return make_response(jsonify(entertainment_controller.find_all()), HTTPStatus.OK)

@entertainment_bp.get('/<int:object_id>')
def get_entertainment(object_id: int) -> Response:
    entertainment = Entertainment.query.filter_by(object_id=object_id).first()

    if entertainment:
        person_info = entertainment.object.put_into_dto()
        entertainment_info = entertainment.put_into_dto()
        combined_info = {**person_info, **entertainment_info}
        return jsonify(combined_info), 200
    else:
        return jsonify({"error": "Entertainment not found"}), 404

@entertainment_bp.put('/<int:object_id>')
def update_entertainment(object_id: int) -> Response:
    content = request.form
    entertainment = Entertainment.create_from_data(content)
    entertainment_controller.update(object_id, entertainment)
    return make_response("Entertainment updated", HTTPStatus.OK)

@entertainment_bp.patch('/<int:object_id>')
def patch_entertainment(object_id: int) -> Response:
    content = request.form
    entertainment_controller.patch(object_id, content)
    return make_response("Entertainment updated", HTTPStatus.OK)

@entertainment_bp.delete('/<int:object_id>')
def delete_entertainment(object_id: int) -> Response:
    entertainment_controller.delete(object_id)
    return make_response("Entertainment deleted", HTTPStatus.OK)

@entertainment_bp.post("")
def create_entertainment() -> Response:
    content = request.form
    entertainment = Entertainment.create_from_data(content)
    entertainment_controller.create(entertainment)
    return make_response("Entertainment created", HTTPStatus.CREATED)

# Additional routes for specific operations related to Entertainment can be added here

