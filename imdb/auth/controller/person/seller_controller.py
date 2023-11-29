from imdb.auth.controller.general_controller import GeneralController
from imdb.auth.service import seller_service

class SellerController(GeneralController):
    _service = seller_service

    def get_seller_info_for_person(self, person_id: int):
        """
        Get seller information for a person.
        :param person_id: ID of the person.
        :return: Seller information as a dictionary.
        """
        return self._service.get_seller_info_for_person(person_id)

    def find_by_person_id(self, person_id):
        pass