from .person.person_dao import PersonDao
from .person.seller_dao import SellerDao
from .object.object_dao import ObjectDao
from .object.hotel_dao import HotelDao
from .menu.menu_dao import MenuDao
from .object.restaurant_dao import RestaurantDao
from .menu.dish_dao import DishDao
from .menu.menu_dish_dao import MenuDishDao
from .object.entertainment_dao import EntertainmentDao
from .person.buyer_dao import BuyerDao
from .object.comments_dao import CommentsDao

person_dao = PersonDao()
seller_dao = SellerDao()
object_dao = ObjectDao()
hotel_dao = HotelDao()
menu_dao = MenuDao()
restaurant_dao = RestaurantDao()
dish_dao = DishDao()
menu_dish_dao = MenuDishDao()
entertainment_dao = EntertainmentDao()
buyer_dao = BuyerDao()
comments_dao = CommentsDao()
