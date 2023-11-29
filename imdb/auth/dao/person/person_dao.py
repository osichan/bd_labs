from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.person.person import Person


class PersonDao(GeneralDAO):
    _domain_type = Person
