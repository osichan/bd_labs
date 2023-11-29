from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.object.object import Object


class ObjectDao(GeneralDAO):
    _domain_type = Object
