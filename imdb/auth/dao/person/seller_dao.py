from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.person.seller import Seller


class SellerDao(GeneralDAO):
    _domain_type = Seller
