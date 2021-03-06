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


class OrderDetailsProduct(object):
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
        'product_id': 'str',
        'name': 'str',
        'index_number': 'int',
        'code': 'str',
        'unit': 'str',
        'unit_multiplier': 'float',
        'qty': 'float',
        'price': 'float',
        'ieps_rate': 'float',
        'comments': 'str',
        'qty_full_filled': 'float',
        'vat_rate': 'float'
    }

    attribute_map = {
        'product_id': 'ProductID',
        'name': 'Name',
        'index_number': 'IndexNumber',
        'code': 'Code',
        'unit': 'Unit',
        'unit_multiplier': 'UnitMultiplier',
        'qty': 'Qty',
        'price': 'Price',
        'ieps_rate': 'IEPSRate',
        'comments': 'Comments',
        'qty_full_filled': 'QtyFullFilled',
        'vat_rate': 'VATRate'
    }

    def __init__(self, product_id=None, name=None, index_number=None, code=None, unit=None, unit_multiplier=None, qty=None, price=None, ieps_rate=None, comments=None, qty_full_filled=None, vat_rate=None):  # noqa: E501
        """OrderDetailsProduct - a model defined in Swagger"""  # noqa: E501

        self._product_id = None
        self._name = None
        self._index_number = None
        self._code = None
        self._unit = None
        self._unit_multiplier = None
        self._qty = None
        self._price = None
        self._ieps_rate = None
        self._comments = None
        self._qty_full_filled = None
        self._vat_rate = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if name is not None:
            self.name = name
        if index_number is not None:
            self.index_number = index_number
        if code is not None:
            self.code = code
        if unit is not None:
            self.unit = unit
        if unit_multiplier is not None:
            self.unit_multiplier = unit_multiplier
        if qty is not None:
            self.qty = qty
        if price is not None:
            self.price = price
        if ieps_rate is not None:
            self.ieps_rate = ieps_rate
        if comments is not None:
            self.comments = comments
        if qty_full_filled is not None:
            self.qty_full_filled = qty_full_filled
        if vat_rate is not None:
            self.vat_rate = vat_rate

    @property
    def product_id(self):
        """Gets the product_id of this OrderDetailsProduct.  # noqa: E501


        :return: The product_id of this OrderDetailsProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this OrderDetailsProduct.


        :param product_id: The product_id of this OrderDetailsProduct.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def name(self):
        """Gets the name of this OrderDetailsProduct.  # noqa: E501


        :return: The name of this OrderDetailsProduct.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrderDetailsProduct.


        :param name: The name of this OrderDetailsProduct.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def index_number(self):
        """Gets the index_number of this OrderDetailsProduct.  # noqa: E501


        :return: The index_number of this OrderDetailsProduct.  # noqa: E501
        :rtype: int
        """
        return self._index_number

    @index_number.setter
    def index_number(self, index_number):
        """Sets the index_number of this OrderDetailsProduct.


        :param index_number: The index_number of this OrderDetailsProduct.  # noqa: E501
        :type: int
        """

        self._index_number = index_number

    @property
    def code(self):
        """Gets the code of this OrderDetailsProduct.  # noqa: E501


        :return: The code of this OrderDetailsProduct.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this OrderDetailsProduct.


        :param code: The code of this OrderDetailsProduct.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def unit(self):
        """Gets the unit of this OrderDetailsProduct.  # noqa: E501


        :return: The unit of this OrderDetailsProduct.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this OrderDetailsProduct.


        :param unit: The unit of this OrderDetailsProduct.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def unit_multiplier(self):
        """Gets the unit_multiplier of this OrderDetailsProduct.  # noqa: E501


        :return: The unit_multiplier of this OrderDetailsProduct.  # noqa: E501
        :rtype: float
        """
        return self._unit_multiplier

    @unit_multiplier.setter
    def unit_multiplier(self, unit_multiplier):
        """Sets the unit_multiplier of this OrderDetailsProduct.


        :param unit_multiplier: The unit_multiplier of this OrderDetailsProduct.  # noqa: E501
        :type: float
        """

        self._unit_multiplier = unit_multiplier

    @property
    def qty(self):
        """Gets the qty of this OrderDetailsProduct.  # noqa: E501


        :return: The qty of this OrderDetailsProduct.  # noqa: E501
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this OrderDetailsProduct.


        :param qty: The qty of this OrderDetailsProduct.  # noqa: E501
        :type: float
        """

        self._qty = qty

    @property
    def price(self):
        """Gets the price of this OrderDetailsProduct.  # noqa: E501


        :return: The price of this OrderDetailsProduct.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderDetailsProduct.


        :param price: The price of this OrderDetailsProduct.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def ieps_rate(self):
        """Gets the ieps_rate of this OrderDetailsProduct.  # noqa: E501


        :return: The ieps_rate of this OrderDetailsProduct.  # noqa: E501
        :rtype: float
        """
        return self._ieps_rate

    @ieps_rate.setter
    def ieps_rate(self, ieps_rate):
        """Sets the ieps_rate of this OrderDetailsProduct.


        :param ieps_rate: The ieps_rate of this OrderDetailsProduct.  # noqa: E501
        :type: float
        """

        self._ieps_rate = ieps_rate

    @property
    def comments(self):
        """Gets the comments of this OrderDetailsProduct.  # noqa: E501


        :return: The comments of this OrderDetailsProduct.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this OrderDetailsProduct.


        :param comments: The comments of this OrderDetailsProduct.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def qty_full_filled(self):
        """Gets the qty_full_filled of this OrderDetailsProduct.  # noqa: E501


        :return: The qty_full_filled of this OrderDetailsProduct.  # noqa: E501
        :rtype: float
        """
        return self._qty_full_filled

    @qty_full_filled.setter
    def qty_full_filled(self, qty_full_filled):
        """Sets the qty_full_filled of this OrderDetailsProduct.


        :param qty_full_filled: The qty_full_filled of this OrderDetailsProduct.  # noqa: E501
        :type: float
        """

        self._qty_full_filled = qty_full_filled

    @property
    def vat_rate(self):
        """Gets the vat_rate of this OrderDetailsProduct.  # noqa: E501


        :return: The vat_rate of this OrderDetailsProduct.  # noqa: E501
        :rtype: float
        """
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, vat_rate):
        """Sets the vat_rate of this OrderDetailsProduct.


        :param vat_rate: The vat_rate of this OrderDetailsProduct.  # noqa: E501
        :type: float
        """

        self._vat_rate = vat_rate

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
        if not isinstance(other, OrderDetailsProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
