from injector import inject

from crmsystem.services import CustomerService, OrderService
from crmsystem.utilities import ErrorProvider
from crmsystem.decorators import Logger

ERRORS = [
    {"errorKey": 1, "errorId": "CRMSVCCTRL001",
        "errorMessage": "Invalid Controller Callback Specified!"},
    {"errorKey": 2, "errorId": "CRMSVCCTRL002",
        "errorMessage": "Invalid Customer / Order Service(s) Specified!"},
]


class CRMSystemServiceController:
    @inject
    def __init__(self, customerService: CustomerService, orderService: OrderService):
        serviceStatus = customerService is not None and \
            orderService is not None

        if not(serviceStatus):
            raise ErrorProvider.get_error(ERRORS, 2)

        self.customerService = customerService
        self.orderService = orderService

    @Logger(opMessage="Service Controller Process")
    def process(self, customer=None):
        customers = self.customerService.get_customers()
        orders = self.orderService.get_orders(customer)

        return customers, orders
