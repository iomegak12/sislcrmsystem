from prettytable import PrettyTable
from crmsystem.utilities import ErrorProvider

ERRORS = [
    {"errorKey": 1, "errorId": "TABGEN001",
        "errorMessage": "Invalid Customer Collection(s) Specified!"},
    {"errorKey": 2, "errorId": "TABGEN002",
        "errorMessage": "Invalid Orders Collection(s) Specified!"},
]


class TableGenerator:
    @staticmethod
    def get_customer_table(customers):
        if customers is None:
            raise ErrorProvider.get_error(ERRORS, 1)

        table = PrettyTable(
            ["Customer #", "Name", "Address", "Credit", "Status"])

        for customer in customers:
            table.add_row([customer.id, customer.name,
                           customer.address, customer.credit, customer.status])

        return table

    @staticmethod
    def get_orders_table(orders):
        if orders is None:
            raise ErrorProvider.get_error(ERRORS, 2)

        table = PrettyTable([
            "Order #", "Order Date", "Customer", "Address", "Amount"])

        for order in orders:
            table.add_row([order.orderId, order.orderDate,
                           order.customer, order.billingAddress, order.amount])

        return table
