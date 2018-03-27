# coding: utf-8

"""
    Bind ERP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InvoiceDetailsService(object):
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
        'index_number': 'int',
        'service_id': 'str',
        'name': 'str',
        'code': 'str',
        'qty': 'float',
        'price': 'float',
        'vat_rate': 'float',
        'discount': 'float'
    }

    attribute_map = {
        'index_number': 'IndexNumber',
        'service_id': 'ServiceID',
        'name': 'Name',
        'code': 'Code',
        'qty': 'Qty',
        'price': 'Price',
        'vat_rate': 'VATRate',
        'discount': 'Discount'
    }

    def __init__(self, index_number=None, service_id=None, name=None, code=None, qty=None, price=None, vat_rate=None, discount=None):  # noqa: E501
        """InvoiceDetailsService - a model defined in Swagger"""  # noqa: E501

        self._index_number = None
        self._service_id = None
        self._name = None
        self._code = None
        self._qty = None
        self._price = None
        self._vat_rate = None
        self._discount = None
        self.discriminator = None

        if index_number is not None:
            self.index_number = index_number
        if service_id is not None:
            self.service_id = service_id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if qty is not None:
            self.qty = qty
        if price is not None:
            self.price = price
        if vat_rate is not None:
            self.vat_rate = vat_rate
        if discount is not None:
            self.discount = discount

    @property
    def index_number(self):
        """Gets the index_number of this InvoiceDetailsService.  # noqa: E501


        :return: The index_number of this InvoiceDetailsService.  # noqa: E501
        :rtype: int
        """
        return self._index_number

    @index_number.setter
    def index_number(self, index_number):
        """Sets the index_number of this InvoiceDetailsService.


        :param index_number: The index_number of this InvoiceDetailsService.  # noqa: E501
        :type: int
        """

        self._index_number = index_number

    @property
    def service_id(self):
        """Gets the service_id of this InvoiceDetailsService.  # noqa: E501


        :return: The service_id of this InvoiceDetailsService.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this InvoiceDetailsService.


        :param service_id: The service_id of this InvoiceDetailsService.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def name(self):
        """Gets the name of this InvoiceDetailsService.  # noqa: E501


        :return: The name of this InvoiceDetailsService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InvoiceDetailsService.


        :param name: The name of this InvoiceDetailsService.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this InvoiceDetailsService.  # noqa: E501


        :return: The code of this InvoiceDetailsService.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InvoiceDetailsService.


        :param code: The code of this InvoiceDetailsService.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def qty(self):
        """Gets the qty of this InvoiceDetailsService.  # noqa: E501


        :return: The qty of this InvoiceDetailsService.  # noqa: E501
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this InvoiceDetailsService.


        :param qty: The qty of this InvoiceDetailsService.  # noqa: E501
        :type: float
        """

        self._qty = qty

    @property
    def price(self):
        """Gets the price of this InvoiceDetailsService.  # noqa: E501


        :return: The price of this InvoiceDetailsService.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InvoiceDetailsService.


        :param price: The price of this InvoiceDetailsService.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def vat_rate(self):
        """Gets the vat_rate of this InvoiceDetailsService.  # noqa: E501


        :return: The vat_rate of this InvoiceDetailsService.  # noqa: E501
        :rtype: float
        """
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, vat_rate):
        """Sets the vat_rate of this InvoiceDetailsService.


        :param vat_rate: The vat_rate of this InvoiceDetailsService.  # noqa: E501
        :type: float
        """

        self._vat_rate = vat_rate

    @property
    def discount(self):
        """Gets the discount of this InvoiceDetailsService.  # noqa: E501


        :return: The discount of this InvoiceDetailsService.  # noqa: E501
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this InvoiceDetailsService.


        :param discount: The discount of this InvoiceDetailsService.  # noqa: E501
        :type: float
        """

        self._discount = discount

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
        if not isinstance(other, InvoiceDetailsService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other