from .person.person_service import PersonService
from .person.seller_service import SellerService
from .object.object_service import ObjectService
from .object.hotel_service import HotelService
from .menu.menu_service import MenuService
from .object.restaurant_service import RestaurantService
from .menu.dish_service import DishService
from .menu.menu_dish_service import MenuDishService
from .object.entertainment_service import EntertainmentService
from .person.buyer_service import BuyerService
from .object.comments_service import CommentsService

person_service = PersonService()
seller_service = SellerService()
object_service = ObjectService()
hotel_service = HotelService()
menu_service = MenuService()
restaurant_service = RestaurantService()
dish_service = DishService()
menu_dish_service = MenuDishService()
entertainment_service = EntertainmentService()
buyer_service = BuyerService()
comments_service = CommentsService()