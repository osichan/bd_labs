# In your RestaurantDao class, add a find_by_id method
from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.object.restaurant import Restaurant

class RestaurantDao(GeneralDAO):
    _domain_type = Restaurant