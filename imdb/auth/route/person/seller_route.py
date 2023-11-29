from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from imdb.auth.controller import seller_controller
from imdb.auth.domain.person.seller import Seller

seller_bp = Blueprint("sellers", __name__, url_prefix="/sellers/")

@seller_bp.get("")
def get_all_sellers() -> Response:
    return make_response(jsonify(seller_controller.find_all()), HTTPStatus.OK)

@seller_bp.get('/<int:person_id>')
def get_seller(person_id: int) -> Response:
    seller = Seller.query.filter_by(person_id=person_id).first()

    if seller:
        person_info = seller.person.put_into_dto()
        seller_info = seller.put_into_dto()
        combined_info = {**person_info, **seller_info}
        return jsonify(combined_info), 200
    else:
        return jsonify({"error": "Seller not found"}), 404

@seller_bp.put('/<int:person_id>')
def update_seller(person_id: int) -> Response:
    content = request.form
    seller = Seller.create_from_data(content)
    seller_controller.update(person_id, seller)
    return make_response("Seller updated", HTTPStatus.OK)

@seller_bp.patch('/<int:person_id>')
def patch_seller(person_id: int) -> Response:
    content = request.form
    seller_controller.patch(person_id, content)
    return make_response("Seller updated", HTTPStatus.OK)

@seller_bp.delete('/<int:person_id>')
def delete_seller(person_id: int) -> Response:
    seller_controller.delete(person_id)
    return make_response("Seller deleted", HTTPStatus.OK)

@seller_bp.post("")
def create_seller() -> Response:
    content = request.form
    seller = Seller.create_from_data(content)
    seller_controller.create(seller)
    return make_response("Seller created", HTTPStatus.CREATED)

# Additional routes for specific operations related to Seller can be added here

