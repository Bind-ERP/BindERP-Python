# coding: utf-8

"""
    Bind ERP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.new_order_product import NewOrderProduct  # noqa: F401,E501
from swagger_client.models.new_order_service import NewOrderService  # noqa: F401,E501


class NewOrder(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address_id': 'str',
        'client_id': 'str',
        'currency_id': 'str',
        'location_id': 'str',
        'order_date': 'datetime',
        'price_list_id': 'str',
        'warehouse_id': 'str',
        'comments': 'str',
        'discount_amount': 'float',
        'discount_type': 'int',
        'doc_number_id': 'str',
        'exchange_rate': 'float',
        'isr_rate': 'float',
        'purchase_order': 'str',
        'vat_rate': 'float',
        'vat_ret_rate': 'float',
        'emails': 'list[str]',
        'products': 'list[NewOrderProduct]',
        'services': 'list[NewOrderService]'
    }

    attribute_map = {
        'address_id': 'AddressID',
        'client_id': 'ClientID',
        'currency_id': 'CurrencyID',
        'location_id': 'LocationID',
        'order_date': 'OrderDate',
        'price_list_id': 'PriceListID',
        'warehouse_id': 'WarehouseID',
        'comments': 'Comments',
        'discount_amount': 'DiscountAmount',
        'discount_type': 'DiscountType',
        'doc_number_id': 'DocNumberID',
        'exchange_rate': 'ExchangeRate',
        'isr_rate': 'ISRRate',
        'purchase_order': 'PurchaseOrder',
        'vat_rate': 'VATRate',
        'vat_ret_rate': 'VATRetRate',
        'emails': 'Emails',
        'products': 'Products',
        'services': 'Services'
    }

    def __init__(self, address_id=None, client_id=None, currency_id=None, location_id=None, order_date=None, price_list_id=None, warehouse_id=None, comments=None, discount_amount=None, discount_type=None, doc_number_id=None, exchange_rate=None, isr_rate=None, purchase_order=None, vat_rate=None, vat_ret_rate=None, emails=None, products=None, services=None):  # noqa: E501
        """NewOrder - a model defined in Swagger"""  # noqa: E501

        self._address_id = None
        self._client_id = None
        self._currency_id = None
        self._location_id = None
        self._order_date = None
        self._price_list_id = None
        self._warehouse_id = None
        self._comments = None
        self._discount_amount = None
        self._discount_type = None
        self._doc_number_id = None
        self._exchange_rate = None
        self._isr_rate = None
        self._purchase_order = None
        self._vat_rate = None
        self._vat_ret_rate = None
        self._emails = None
        self._products = None
        self._services = None
        self.discriminator = None

        self.address_id = address_id
        self.client_id = client_id
        self.currency_id = currency_id
        self.location_id = location_id
        self.order_date = order_date
        self.price_list_id = price_list_id
        self.warehouse_id = warehouse_id
        if comments is not None:
            self.comments = comments
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if discount_type is not None:
            self.discount_type = discount_type
        if doc_number_id is not None:
            self.doc_number_id = doc_number_id
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if isr_rate is not None:
            self.isr_rate = isr_rate
        if purchase_order is not None:
            self.purchase_order = purchase_order
        if vat_rate is not None:
            self.vat_rate = vat_rate
        if vat_ret_rate is not None:
            self.vat_ret_rate = vat_ret_rate
        if emails is not None:
            self.emails = emails
        if products is not None:
            self.products = products
        if services is not None:
            self.services = services

    @property
    def address_id(self):
        """Gets the address_id of this NewOrder.  # noqa: E501


        :return: The address_id of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """Sets the address_id of this NewOrder.


        :param address_id: The address_id of this NewOrder.  # noqa: E501
        :type: str
        """
        if address_id is None:
            raise ValueError("Invalid value for `address_id`, must not be `None`")  # noqa: E501

        self._address_id = address_id

    @property
    def client_id(self):
        """Gets the client_id of this NewOrder.  # noqa: E501


        :return: The client_id of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this NewOrder.


        :param client_id: The client_id of this NewOrder.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def currency_id(self):
        """Gets the currency_id of this NewOrder.  # noqa: E501


        :return: The currency_id of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this NewOrder.


        :param currency_id: The currency_id of this NewOrder.  # noqa: E501
        :type: str
        """
        if currency_id is None:
            raise ValueError("Invalid value for `currency_id`, must not be `None`")  # noqa: E501

        self._currency_id = currency_id

    @property
    def location_id(self):
        """Gets the location_id of this NewOrder.  # noqa: E501


        :return: The location_id of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this NewOrder.


        :param location_id: The location_id of this NewOrder.  # noqa: E501
        :type: str
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def order_date(self):
        """Gets the order_date of this NewOrder.  # noqa: E501


        :return: The order_date of this NewOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this NewOrder.


        :param order_date: The order_date of this NewOrder.  # noqa: E501
        :type: datetime
        """
        if order_date is None:
            raise ValueError("Invalid value for `order_date`, must not be `None`")  # noqa: E501

        self._order_date = order_date

    @property
    def price_list_id(self):
        """Gets the price_list_id of this NewOrder.  # noqa: E501


        :return: The price_list_id of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._price_list_id

    @price_list_id.setter
    def price_list_id(self, price_list_id):
        """Sets the price_list_id of this NewOrder.


        :param price_list_id: The price_list_id of this NewOrder.  # noqa: E501
        :type: str
        """
        if price_list_id is None:
            raise ValueError("Invalid value for `price_list_id`, must not be `None`")  # noqa: E501

        self._price_list_id = price_list_id

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this NewOrder.  # noqa: E501


        :return: The warehouse_id of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this NewOrder.


        :param warehouse_id: The warehouse_id of this NewOrder.  # noqa: E501
        :type: str
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def comments(self):
        """Gets the comments of this NewOrder.  # noqa: E501


        :return: The comments of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this NewOrder.


        :param comments: The comments of this NewOrder.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def discount_amount(self):
        """Gets the discount_amount of this NewOrder.  # noqa: E501


        :return: The discount_amount of this NewOrder.  # noqa: E501
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this NewOrder.


        :param discount_amount: The discount_amount of this NewOrder.  # noqa: E501
        :type: float
        """

        self._discount_amount = discount_amount

    @property
    def discount_type(self):
        """Gets the discount_type of this NewOrder.  # noqa: E501


        :return: The discount_type of this NewOrder.  # noqa: E501
        :rtype: int
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this NewOrder.


        :param discount_type: The discount_type of this NewOrder.  # noqa: E501
        :type: int
        """

        self._discount_type = discount_type

    @property
    def doc_number_id(self):
        """Gets the doc_number_id of this NewOrder.  # noqa: E501


        :return: The doc_number_id of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._doc_number_id

    @doc_number_id.setter
    def doc_number_id(self, doc_number_id):
        """Sets the doc_number_id of this NewOrder.


        :param doc_number_id: The doc_number_id of this NewOrder.  # noqa: E501
        :type: str
        """

        self._doc_number_id = doc_number_id

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this NewOrder.  # noqa: E501


        :return: The exchange_rate of this NewOrder.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this NewOrder.


        :param exchange_rate: The exchange_rate of this NewOrder.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def isr_rate(self):
        """Gets the isr_rate of this NewOrder.  # noqa: E501


        :return: The isr_rate of this NewOrder.  # noqa: E501
        :rtype: float
        """
        return self._isr_rate

    @isr_rate.setter
    def isr_rate(self, isr_rate):
        """Sets the isr_rate of this NewOrder.


        :param isr_rate: The isr_rate of this NewOrder.  # noqa: E501
        :type: float
        """

        self._isr_rate = isr_rate

    @property
    def purchase_order(self):
        """Gets the purchase_order of this NewOrder.  # noqa: E501


        :return: The purchase_order of this NewOrder.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """Sets the purchase_order of this NewOrder.


        :param purchase_order: The purchase_order of this NewOrder.  # noqa: E501
        :type: str
        """

        self._purchase_order = purchase_order

    @property
    def vat_rate(self):
        """Gets the vat_rate of this NewOrder.  # noqa: E501


        :return: The vat_rate of this NewOrder.  # noqa: E501
        :rtype: float
        """
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, vat_rate):
        """Sets the vat_rate of this NewOrder.


        :param vat_rate: The vat_rate of this NewOrder.  # noqa: E501
        :type: float
        """

        self._vat_rate = vat_rate

    @property
    def vat_ret_rate(self):
        """Gets the vat_ret_rate of this NewOrder.  # noqa: E501


        :return: The vat_ret_rate of this NewOrder.  # noqa: E501
        :rtype: float
        """
        return self._vat_ret_rate

    @vat_ret_rate.setter
    def vat_ret_rate(self, vat_ret_rate):
        """Sets the vat_ret_rate of this NewOrder.


        :param vat_ret_rate: The vat_ret_rate of this NewOrder.  # noqa: E501
        :type: float
        """

        self._vat_ret_rate = vat_ret_rate

    @property
    def emails(self):
        """Gets the emails of this NewOrder.  # noqa: E501


        :return: The emails of this NewOrder.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this NewOrder.


        :param emails: The emails of this NewOrder.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def products(self):
        """Gets the products of this NewOrder.  # noqa: E501


        :return: The products of this NewOrder.  # noqa: E501
        :rtype: list[NewOrderProduct]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this NewOrder.


        :param products: The products of this NewOrder.  # noqa: E501
        :type: list[NewOrderProduct]
        """

        self._products = products

    @property
    def services(self):
        """Gets the services of this NewOrder.  # noqa: E501


        :return: The services of this NewOrder.  # noqa: E501
        :rtype: list[NewOrderService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this NewOrder.


        :param services: The services of this NewOrder.  # noqa: E501
        :type: list[NewOrderService]
        """

        self._services = services

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
