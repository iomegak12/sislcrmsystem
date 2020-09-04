import json
from flask import Flask

from crmsystem.config import GlobalConfiguration
from crmsystem.constants import GlobalConstants
from crmsystem.services import CustomerService, OrderService
from crmsystem.utilities import CustomerEncoder, OrderEncoder

configuration = GlobalConfiguration.get_configuration()
flaskApp = Flask(__name__)
flaskApp.config["DEBUG"] = int(configuration[GlobalConstants.FLASK_DEBUG])


class CRMSystemApi:
    @staticmethod
    @flaskApp.route("/", methods=["GET"])
    def home():
        return "<h1> CRM System Home </h1>"

    @staticmethod
    @flaskApp.route("/api/v1/customers/", methods=["GET"])
    def get_customers():
        service = CustomerService()
        customerProfiles = service.get_customers()

        return json.dumps(customerProfiles, cls=CustomerEncoder)

    @ staticmethod
    @ flaskApp.route("/api/v1/orders/", methods=["GET"])
    def get_orders():
        service = OrderService()
        orders = service.get_orders()

        return json.dumps(orders, cls=OrderEncoder)

    @ staticmethod
    @ flaskApp.route("/api/v1/orders/<customerid>", methods=["GET"])
    def get_orders_by_customer(customerid: int):
        service = OrderService()
        orders = service.get_orders(customerid)

        return json.dumps(orders, cls=OrderEncoder)
