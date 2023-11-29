from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from imdb.auth.controller import comments_controller
from imdb.auth.domain.object.comments import Comments

comments_bp = Blueprint("comments", __name__, url_prefix="/comments/")

@comments_bp.get("")
def get_all_comments() -> Response:
    return make_response(jsonify(comments_controller.find_all()), HTTPStatus.OK)

@comments_bp.get('/<int:object_id>')
def get_comment(object_id: int) -> Response:
    return make_response(jsonify(comments_controller.find_by_id(object_id)), HTTPStatus.OK)

@comments_bp.put('/<int:object_id>')
def update_comment(object_id: int) -> Response:
    content = request.form
    comment = Comments.create_from_data(content)
    comments_controller.update(object_id, comment)
    return make_response("Comment updated", HTTPStatus.OK)

@comments_bp.patch('/<int:object_id>')
def patch_comment(object_id: int) -> Response:
    content = request.form
    comments_controller.patch(object_id, content)
    return make_response("Comment updated", HTTPStatus.OK)

@comments_bp.delete('/<int:object_id>')
def delete_comment(object_id: int) -> Response:
    comments_controller.delete(object_id)
    return make_response("Comment deleted", HTTPStatus.OK)

@comments_bp.post("")
def create_comment() -> Response:
    content = request.form
    comment = Comments.create_from_data(content)
    comments_controller.create(comment)
    return make_response("Comment created", HTTPStatus.CREATED)

# Additional routes for specific operations related to Comments can be added here

