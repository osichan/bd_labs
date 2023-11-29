from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.object.hotel import Hotel


class HotelDao(GeneralDAO):
    _domain_type = Hotel
