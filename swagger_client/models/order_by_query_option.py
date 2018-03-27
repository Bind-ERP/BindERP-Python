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

from swagger_client.models.o_data_query_context import ODataQueryContext  # noqa: F401,E501
from swagger_client.models.order_by_clause import OrderByClause  # noqa: F401,E501
from swagger_client.models.order_by_node import OrderByNode  # noqa: F401,E501
from swagger_client.models.order_by_query_validator import OrderByQueryValidator  # noqa: F401,E501


class OrderByQueryOption(object):
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
        'context': 'ODataQueryContext',
        'order_by_nodes': 'list[OrderByNode]',
        'raw_value': 'str',
        'validator': 'OrderByQueryValidator',
        'order_by_clause': 'OrderByClause'
    }

    attribute_map = {
        'context': 'Context',
        'order_by_nodes': 'OrderByNodes',
        'raw_value': 'RawValue',
        'validator': 'Validator',
        'order_by_clause': 'OrderByClause'
    }

    def __init__(self, context=None, order_by_nodes=None, raw_value=None, validator=None, order_by_clause=None):  # noqa: E501
        """OrderByQueryOption - a model defined in Swagger"""  # noqa: E501

        self._context = None
        self._order_by_nodes = None
        self._raw_value = None
        self._validator = None
        self._order_by_clause = None
        self.discriminator = None

        if context is not None:
            self.context = context
        if order_by_nodes is not None:
            self.order_by_nodes = order_by_nodes
        if raw_value is not None:
            self.raw_value = raw_value
        if validator is not None:
            self.validator = validator
        if order_by_clause is not None:
            self.order_by_clause = order_by_clause

    @property
    def context(self):
        """Gets the context of this OrderByQueryOption.  # noqa: E501


        :return: The context of this OrderByQueryOption.  # noqa: E501
        :rtype: ODataQueryContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this OrderByQueryOption.


        :param context: The context of this OrderByQueryOption.  # noqa: E501
        :type: ODataQueryContext
        """

        self._context = context

    @property
    def order_by_nodes(self):
        """Gets the order_by_nodes of this OrderByQueryOption.  # noqa: E501


        :return: The order_by_nodes of this OrderByQueryOption.  # noqa: E501
        :rtype: list[OrderByNode]
        """
        return self._order_by_nodes

    @order_by_nodes.setter
    def order_by_nodes(self, order_by_nodes):
        """Sets the order_by_nodes of this OrderByQueryOption.


        :param order_by_nodes: The order_by_nodes of this OrderByQueryOption.  # noqa: E501
        :type: list[OrderByNode]
        """

        self._order_by_nodes = order_by_nodes

    @property
    def raw_value(self):
        """Gets the raw_value of this OrderByQueryOption.  # noqa: E501


        :return: The raw_value of this OrderByQueryOption.  # noqa: E501
        :rtype: str
        """
        return self._raw_value

    @raw_value.setter
    def raw_value(self, raw_value):
        """Sets the raw_value of this OrderByQueryOption.


        :param raw_value: The raw_value of this OrderByQueryOption.  # noqa: E501
        :type: str
        """

        self._raw_value = raw_value

    @property
    def validator(self):
        """Gets the validator of this OrderByQueryOption.  # noqa: E501


        :return: The validator of this OrderByQueryOption.  # noqa: E501
        :rtype: OrderByQueryValidator
        """
        return self._validator

    @validator.setter
    def validator(self, validator):
        """Sets the validator of this OrderByQueryOption.


        :param validator: The validator of this OrderByQueryOption.  # noqa: E501
        :type: OrderByQueryValidator
        """

        self._validator = validator

    @property
    def order_by_clause(self):
        """Gets the order_by_clause of this OrderByQueryOption.  # noqa: E501


        :return: The order_by_clause of this OrderByQueryOption.  # noqa: E501
        :rtype: OrderByClause
        """
        return self._order_by_clause

    @order_by_clause.setter
    def order_by_clause(self, order_by_clause):
        """Sets the order_by_clause of this OrderByQueryOption.


        :param order_by_clause: The order_by_clause of this OrderByQueryOption.  # noqa: E501
        :type: OrderByClause
        """

        self._order_by_clause = order_by_clause

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
        if not isinstance(other, OrderByQueryOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other