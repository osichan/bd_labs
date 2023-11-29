from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.menu.dish import Dish


class DishDao(GeneralDAO):
    _domain_type = Dish
