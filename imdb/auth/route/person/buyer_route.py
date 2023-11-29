from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from imdb.auth.controller import buyer_controller
from imdb.auth.domain.person.buyer import Buyer

buyer_bp = Blueprint("buyers", __name__, url_prefix="/buyers/")

@buyer_bp.get("")
def get_all_buyers() -> Response:
    return make_response(jsonify(buyer_controller.find_all()), HTTPStatus.OK)

@buyer_bp.get('/<int:person_id>')
def get_seller(person_id: int) -> Response:
    buyer = Buyer.query.filter_by(person_id=person_id).first()

    if buyer:
        person_info = buyer.person.put_into_dto()
        buyer_info = buyer.put_into_dto()
        combined_info = {**person_info, **buyer_info}
        return jsonify(combined_info), 200
    else:
        return jsonify({"error": "Buyer not found"}), 404

@buyer_bp.put('/<int:person_id>')
def update_buyer(person_id: int) -> Response:
    content = request.form
    buyer = Buyer.create_from_data(content)
    buyer_controller.update(person_id, buyer)
    return make_response("Buyer updated", HTTPStatus.OK)

@buyer_bp.patch('/<int:person_id>')
def patch_buyer(person_id: int) -> Response:
    content = request.form
    buyer_controller.patch(person_id, content)
    return make_response("Buyer updated", HTTPStatus.OK)

@buyer_bp.delete('/<int:person_id>')
def delete_buyer(person_id: int) -> Response:
    buyer_controller.delete(person_id)
    return make_response("Buyer deleted", HTTPStatus.OK)

@buyer_bp.post("")
def create_buyer() -> Response:
    content = request.form
    buyer = Buyer.create_from_data(content)
    buyer_controller.create(buyer)
    return make_response("Buyer created", HTTPStatus.CREATED)

# Additional routes for specific operations related to Buyer can be added here

