from imdb.auth.controller.general_controller import GeneralController
from imdb.auth.service import person_service

class PersonController(GeneralController):
    _service = person_service

    def get_buyer_info(self, person_id: int):
        return self._service.get_buyer_info_for_person(person_id)

    def get_seller_info(self, person_id: int):
        """
        Get seller information for a person.
        :param person_id: ID of the person.
        :return: Seller information as a dictionary.
        """
        return self._service.get_seller_info_for_person(person_id)
