from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.object.entertainment import Entertainment


class EntertainmentDao(GeneralDAO):
    _domain_type = Entertainment
