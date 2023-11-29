from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from imdb.auth.controller import person_controller
from imdb.auth.domain.person.person import Person

person_bp = Blueprint("persons", __name__, url_prefix="/persons/")

@person_bp.get("")
def get_all_persons() -> Response:
    return make_response(jsonify(person_controller.find_all()), HTTPStatus.OK)

@person_bp.get('/<int:person_id>')
def get_person(person_id: int) -> Response:
    return make_response(jsonify(person_controller.find_by_id(person_id)), HTTPStatus.OK)

@person_bp.put('/<int:person_id>')
def update_person(person_id: int) -> Response:
    content = request.form
    person = Person.create_from_data(content)
    person_controller.update(person_id, person)
    return make_response("Person updated", HTTPStatus.OK)

@person_bp.patch('/<int:person_id>')
def patch_person(person_id: int) -> Response:
    content = request.form
    person_controller.patch(person_id, content)
    return make_response("Person updated", HTTPStatus.OK)

@person_bp.delete('/<int:person_id>')
def delete_person(person_id: int) -> Response:
    person_controller.delete(person_id)
    return make_response("Person deleted", HTTPStatus.OK)

@person_bp.post("")
def create_person() -> Response:
    content = request.form
    person = Person.create_from_data(content)
    person_id = person_controller.create(person)
    return make_response(f"Person created with ID: {person_id}", HTTPStatus.CREATED)

# Additional routes for specific operations related to Person can be added here

