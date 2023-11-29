from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.person.buyer import Buyer


class BuyerDao(GeneralDAO):
    _domain_type = Buyer
