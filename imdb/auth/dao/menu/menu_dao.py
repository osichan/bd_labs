from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.menu.menu import Menu


class MenuDao(GeneralDAO):
    _domain_type = Menu
