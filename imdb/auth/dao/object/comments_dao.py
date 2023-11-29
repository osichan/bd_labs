from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.object.comments import Comments


class CommentsDao(GeneralDAO):
    _domain_type = Comments
