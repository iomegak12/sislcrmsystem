import requests
import json

from crmsystem.config import GlobalConfiguration
from crmsystem.utilities import ErrorProvider, CustomerEncoder
from crmsystem.models import CustomerProfile
from crmsystem.constants import GlobalConstants

ERRORS = [
    {"errorKey": 1, "errorId": "CUSTSVC001",
        "errorMessage": "Invalid Customer Service Callback Specified!"},
    {"errorKey": 2, "errorId": "CUSTSVC002",
        "errorMessage": "Invalid Customer Service URL Specified!"},
]


class CustomerService():
    def __init__(self):
        configuration = GlobalConfiguration.get_configuration()
        customerServiceUrl = configuration[GlobalConstants.CUSTOMER_SERVICE_URL]

        if customerServiceUrl is None:
            raise ErrorProvider.get_error(ERRORS, 2)

        self.customerServiceUrl = customerServiceUrl

    def get_customers(self):
        response = requests.get(self.customerServiceUrl)
        responseText = response.text
        processedCustomerProfiles = json.loads(
            responseText, object_hook=CustomerEncoder.transform)

        return processedCustomerProfiles
