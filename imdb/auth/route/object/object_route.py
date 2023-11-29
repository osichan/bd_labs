from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from imdb.auth.controller import object_controller
from imdb.auth.domain.object.object import Object

object_bp = Blueprint("objects", __name__, url_prefix="/objects/")

@object_bp.get("")
def get_all_objects() -> Response:
    return make_response(jsonify(object_controller.find_all()), HTTPStatus.OK)

@object_bp.get('/<int:object_id>')
def get_object(object_id: int) -> Response:
    return make_response(jsonify(object_controller.find_by_id(object_id)), HTTPStatus.OK)

@object_bp.put('/<int:object_id>')
def update_object(object_id: int) -> Response:
    content = request.form
    obj = Object.create_from_data(content)
    object_controller.update(object_id, obj)
    return make_response("Object updated", HTTPStatus.OK)

@object_bp.patch('/<int:object_id>')
def patch_object(object_id: int) -> Response:
    content = request.form
    object_controller.patch(object_id, content)
    return make_response("Object updated", HTTPStatus.OK)

@object_bp.delete('/<int:object_id>')
def delete_object(object_id: int) -> Response:
    object_controller.delete(object_id)
    return make_response("Object deleted", HTTPStatus.OK)

@object_bp.post("")
def create_object() -> Response:
    content = request.form
    obj = Object.create_from_data(content)
    object_id = object_controller.create(obj)
    return make_response(f"Object created with ID: {object_id}", HTTPStatus.CREATED)

# Additional routes for specific operations related to Object can be added here

