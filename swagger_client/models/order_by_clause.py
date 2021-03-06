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

from swagger_client.models.i_edm_type_reference import IEdmTypeReference  # noqa: F401,E501
from swagger_client.models.order_by_clause import OrderByClause  # noqa: F401,E501
from swagger_client.models.range_variable import RangeVariable  # noqa: F401,E501
from swagger_client.models.single_value_node import SingleValueNode  # noqa: F401,E501


class OrderByClause(object):
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
        'then_by': 'OrderByClause',
        'expression': 'SingleValueNode',
        'direction': 'str',
        'range_variable': 'RangeVariable',
        'item_type': 'IEdmTypeReference'
    }

    attribute_map = {
        'then_by': 'ThenBy',
        'expression': 'Expression',
        'direction': 'Direction',
        'range_variable': 'RangeVariable',
        'item_type': 'ItemType'
    }

    def __init__(self, then_by=None, expression=None, direction=None, range_variable=None, item_type=None):  # noqa: E501
        """OrderByClause - a model defined in Swagger"""  # noqa: E501

        self._then_by = None
        self._expression = None
        self._direction = None
        self._range_variable = None
        self._item_type = None
        self.discriminator = None

        if then_by is not None:
            self.then_by = then_by
        if expression is not None:
            self.expression = expression
        if direction is not None:
            self.direction = direction
        if range_variable is not None:
            self.range_variable = range_variable
        if item_type is not None:
            self.item_type = item_type

    @property
    def then_by(self):
        """Gets the then_by of this OrderByClause.  # noqa: E501


        :return: The then_by of this OrderByClause.  # noqa: E501
        :rtype: OrderByClause
        """
        return self._then_by

    @then_by.setter
    def then_by(self, then_by):
        """Sets the then_by of this OrderByClause.


        :param then_by: The then_by of this OrderByClause.  # noqa: E501
        :type: OrderByClause
        """

        self._then_by = then_by

    @property
    def expression(self):
        """Gets the expression of this OrderByClause.  # noqa: E501


        :return: The expression of this OrderByClause.  # noqa: E501
        :rtype: SingleValueNode
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this OrderByClause.


        :param expression: The expression of this OrderByClause.  # noqa: E501
        :type: SingleValueNode
        """

        self._expression = expression

    @property
    def direction(self):
        """Gets the direction of this OrderByClause.  # noqa: E501


        :return: The direction of this OrderByClause.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this OrderByClause.


        :param direction: The direction of this OrderByClause.  # noqa: E501
        :type: str
        """
        allowed_values = ["Ascending", "Descending"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def range_variable(self):
        """Gets the range_variable of this OrderByClause.  # noqa: E501


        :return: The range_variable of this OrderByClause.  # noqa: E501
        :rtype: RangeVariable
        """
        return self._range_variable

    @range_variable.setter
    def range_variable(self, range_variable):
        """Sets the range_variable of this OrderByClause.


        :param range_variable: The range_variable of this OrderByClause.  # noqa: E501
        :type: RangeVariable
        """

        self._range_variable = range_variable

    @property
    def item_type(self):
        """Gets the item_type of this OrderByClause.  # noqa: E501


        :return: The item_type of this OrderByClause.  # noqa: E501
        :rtype: IEdmTypeReference
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this OrderByClause.


        :param item_type: The item_type of this OrderByClause.  # noqa: E501
        :type: IEdmTypeReference
        """

        self._item_type = item_type

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
        if not isinstance(other, OrderByClause):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
