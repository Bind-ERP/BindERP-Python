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


class ProductPricesItems(object):
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
        'name': 'str',
        'margin': 'float',
        'price': 'float',
        'currency_code': 'str',
        'type': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'margin': 'Margin',
        'price': 'Price',
        'currency_code': 'CurrencyCode',
        'type': 'Type'
    }

    def __init__(self, name=None, margin=None, price=None, currency_code=None, type=None):  # noqa: E501
        """ProductPricesItems - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._margin = None
        self._price = None
        self._currency_code = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if margin is not None:
            self.margin = margin
        if price is not None:
            self.price = price
        if currency_code is not None:
            self.currency_code = currency_code
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this ProductPricesItems.  # noqa: E501


        :return: The name of this ProductPricesItems.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductPricesItems.


        :param name: The name of this ProductPricesItems.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def margin(self):
        """Gets the margin of this ProductPricesItems.  # noqa: E501


        :return: The margin of this ProductPricesItems.  # noqa: E501
        :rtype: float
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """Sets the margin of this ProductPricesItems.


        :param margin: The margin of this ProductPricesItems.  # noqa: E501
        :type: float
        """

        self._margin = margin

    @property
    def price(self):
        """Gets the price of this ProductPricesItems.  # noqa: E501


        :return: The price of this ProductPricesItems.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ProductPricesItems.


        :param price: The price of this ProductPricesItems.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def currency_code(self):
        """Gets the currency_code of this ProductPricesItems.  # noqa: E501


        :return: The currency_code of this ProductPricesItems.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this ProductPricesItems.


        :param currency_code: The currency_code of this ProductPricesItems.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def type(self):
        """Gets the type of this ProductPricesItems.  # noqa: E501


        :return: The type of this ProductPricesItems.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProductPricesItems.


        :param type: The type of this ProductPricesItems.  # noqa: E501
        :type: int
        """

        self._type = type

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
        if not isinstance(other, ProductPricesItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
