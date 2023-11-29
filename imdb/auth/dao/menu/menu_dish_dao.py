from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.menu.menu_dish import MenuDish


class MenuDishDao(GeneralDAO):
    _domain_type = MenuDish
