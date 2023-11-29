from http import HTTPStatus
from flask import abort
from imdb.auth.dao import comments_dao
from imdb.auth.service.general_service import GeneralService


class CommentsService(GeneralService):
    _dao = comments_dao

    def get_comments_info(self, comments_id: int):
        comments = self._dao.find_by_id(comments_id)
        if comments is None:
            abort(HTTPStatus.NOT_FOUND)

        comments_info = {
            "object_id": comments.object_id,
            "buyer_person_id": comments.buyer_person_id,
            "comment": comments.comment,
            # Add other relevant fields from the Comments model
        }

        return comments_info
