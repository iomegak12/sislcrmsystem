import json
from .error_provider import ErrorProvider
from crmsystem.models import CustomerProfile

ERRORS = [
    {"errorKey": 1, "errorId": "CUSTTRANS001",
        "errorMessage": "Invalid Customer Dictionary Provided"},
]


class CustomerEncoder(json.JSONEncoder):
    @staticmethod
    def transform(dictionary):
        if dictionary is None:
            raise ErrorProvider.get_error(ERRORS, 1)

        customerProfile = CustomerProfile(
            dictionary["id"], dictionary["name"], dictionary["address"],
            dictionary["credit"], dictionary["status"], dictionary["remarks"])

        return customerProfile

    def default(self, o):
        return o.__dict__
