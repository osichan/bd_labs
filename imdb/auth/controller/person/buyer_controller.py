from imdb.auth.controller.general_controller import GeneralController
from imdb.auth.service import buyer_service

class BuyerController(GeneralController):
    _service = buyer_service

    def get_buyer_info_for_person(self, person_id: int):
        """
        Get buyer information for a person.
        :param person_id: ID of the person.
        :return: Buyer information as a dictionary.
        """

        return self._service.get_buyer_info_for_person(person_id)

    def find_by_person_id(self, person_id):
        pass