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

from swagger_client.models.o_data_query_context import ODataQueryContext  # noqa: F401,E501
from swagger_client.models.select_expand_clause import SelectExpandClause  # noqa: F401,E501
from swagger_client.models.select_expand_query_validator import SelectExpandQueryValidator  # noqa: F401,E501


class SelectExpandQueryOption(object):
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
        'raw_select': 'str',
        'raw_expand': 'str',
        'validator': 'SelectExpandQueryValidator',
        'select_expand_clause': 'SelectExpandClause'
    }

    attribute_map = {
        'context': 'Context',
        'raw_select': 'RawSelect',
        'raw_expand': 'RawExpand',
        'validator': 'Validator',
        'select_expand_clause': 'SelectExpandClause'
    }

    def __init__(self, context=None, raw_select=None, raw_expand=None, validator=None, select_expand_clause=None):  # noqa: E501
        """SelectExpandQueryOption - a model defined in Swagger"""  # noqa: E501

        self._context = None
        self._raw_select = None
        self._raw_expand = None
        self._validator = None
        self._select_expand_clause = None
        self.discriminator = None

        if context is not None:
            self.context = context
        if raw_select is not None:
            self.raw_select = raw_select
        if raw_expand is not None:
            self.raw_expand = raw_expand
        if validator is not None:
            self.validator = validator
        if select_expand_clause is not None:
            self.select_expand_clause = select_expand_clause

    @property
    def context(self):
        """Gets the context of this SelectExpandQueryOption.  # noqa: E501


        :return: The context of this SelectExpandQueryOption.  # noqa: E501
        :rtype: ODataQueryContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this SelectExpandQueryOption.


        :param context: The context of this SelectExpandQueryOption.  # noqa: E501
        :type: ODataQueryContext
        """

        self._context = context

    @property
    def raw_select(self):
        """Gets the raw_select of this SelectExpandQueryOption.  # noqa: E501


        :return: The raw_select of this SelectExpandQueryOption.  # noqa: E501
        :rtype: str
        """
        return self._raw_select

    @raw_select.setter
    def raw_select(self, raw_select):
        """Sets the raw_select of this SelectExpandQueryOption.


        :param raw_select: The raw_select of this SelectExpandQueryOption.  # noqa: E501
        :type: str
        """

        self._raw_select = raw_select

    @property
    def raw_expand(self):
        """Gets the raw_expand of this SelectExpandQueryOption.  # noqa: E501


        :return: The raw_expand of this SelectExpandQueryOption.  # noqa: E501
        :rtype: str
        """
        return self._raw_expand

    @raw_expand.setter
    def raw_expand(self, raw_expand):
        """Sets the raw_expand of this SelectExpandQueryOption.


        :param raw_expand: The raw_expand of this SelectExpandQueryOption.  # noqa: E501
        :type: str
        """

        self._raw_expand = raw_expand

    @property
    def validator(self):
        """Gets the validator of this SelectExpandQueryOption.  # noqa: E501


        :return: The validator of this SelectExpandQueryOption.  # noqa: E501
        :rtype: SelectExpandQueryValidator
        """
        return self._validator

    @validator.setter
    def validator(self, validator):
        """Sets the validator of this SelectExpandQueryOption.


        :param validator: The validator of this SelectExpandQueryOption.  # noqa: E501
        :type: SelectExpandQueryValidator
        """

        self._validator = validator

    @property
    def select_expand_clause(self):
        """Gets the select_expand_clause of this SelectExpandQueryOption.  # noqa: E501


        :return: The select_expand_clause of this SelectExpandQueryOption.  # noqa: E501
        :rtype: SelectExpandClause
        """
        return self._select_expand_clause

    @select_expand_clause.setter
    def select_expand_clause(self, select_expand_clause):
        """Sets the select_expand_clause of this SelectExpandQueryOption.


        :param select_expand_clause: The select_expand_clause of this SelectExpandQueryOption.  # noqa: E501
        :type: SelectExpandClause
        """

        self._select_expand_clause = select_expand_clause

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
        if not isinstance(other, SelectExpandQueryOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
