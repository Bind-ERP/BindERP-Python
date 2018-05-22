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

from swagger_client.models.filter_query_option import FilterQueryOption  # noqa: F401,E501
from swagger_client.models.inline_count_query_option import InlineCountQueryOption  # noqa: F401,E501
from swagger_client.models.o_data_query_context import ODataQueryContext  # noqa: F401,E501
from swagger_client.models.o_data_query_validator import ODataQueryValidator  # noqa: F401,E501
from swagger_client.models.o_data_raw_query_options import ODataRawQueryOptions  # noqa: F401,E501
from swagger_client.models.order_by_query_option import OrderByQueryOption  # noqa: F401,E501
from swagger_client.models.select_expand_query_option import SelectExpandQueryOption  # noqa: F401,E501
from swagger_client.models.skip_query_option import SkipQueryOption  # noqa: F401,E501
from swagger_client.models.top_query_option import TopQueryOption  # noqa: F401,E501


class ODataQueryOptionsProviderListItem(object):
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
        'if_match': 'object',
        'if_none_match': 'object',
        'context': 'ODataQueryContext',
        'request': 'object',
        'raw_values': 'ODataRawQueryOptions',
        'select_expand': 'SelectExpandQueryOption',
        'filter': 'FilterQueryOption',
        'order_by': 'OrderByQueryOption',
        'skip': 'SkipQueryOption',
        'top': 'TopQueryOption',
        'inline_count': 'InlineCountQueryOption',
        'validator': 'ODataQueryValidator'
    }

    attribute_map = {
        'if_match': 'IfMatch',
        'if_none_match': 'IfNoneMatch',
        'context': 'Context',
        'request': 'Request',
        'raw_values': 'RawValues',
        'select_expand': 'SelectExpand',
        'filter': 'Filter',
        'order_by': 'OrderBy',
        'skip': 'Skip',
        'top': 'Top',
        'inline_count': 'InlineCount',
        'validator': 'Validator'
    }

    def __init__(self, if_match=None, if_none_match=None, context=None, request=None, raw_values=None, select_expand=None, filter=None, order_by=None, skip=None, top=None, inline_count=None, validator=None):  # noqa: E501
        """ODataQueryOptionsProviderListItem - a model defined in Swagger"""  # noqa: E501

        self._if_match = None
        self._if_none_match = None
        self._context = None
        self._request = None
        self._raw_values = None
        self._select_expand = None
        self._filter = None
        self._order_by = None
        self._skip = None
        self._top = None
        self._inline_count = None
        self._validator = None
        self.discriminator = None

        if if_match is not None:
            self.if_match = if_match
        if if_none_match is not None:
            self.if_none_match = if_none_match
        if context is not None:
            self.context = context
        if request is not None:
            self.request = request
        if raw_values is not None:
            self.raw_values = raw_values
        if select_expand is not None:
            self.select_expand = select_expand
        if filter is not None:
            self.filter = filter
        if order_by is not None:
            self.order_by = order_by
        if skip is not None:
            self.skip = skip
        if top is not None:
            self.top = top
        if inline_count is not None:
            self.inline_count = inline_count
        if validator is not None:
            self.validator = validator

    @property
    def if_match(self):
        """Gets the if_match of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The if_match of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: object
        """
        return self._if_match

    @if_match.setter
    def if_match(self, if_match):
        """Sets the if_match of this ODataQueryOptionsProviderListItem.


        :param if_match: The if_match of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: object
        """

        self._if_match = if_match

    @property
    def if_none_match(self):
        """Gets the if_none_match of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The if_none_match of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: object
        """
        return self._if_none_match

    @if_none_match.setter
    def if_none_match(self, if_none_match):
        """Sets the if_none_match of this ODataQueryOptionsProviderListItem.


        :param if_none_match: The if_none_match of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: object
        """

        self._if_none_match = if_none_match

    @property
    def context(self):
        """Gets the context of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The context of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: ODataQueryContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ODataQueryOptionsProviderListItem.


        :param context: The context of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: ODataQueryContext
        """

        self._context = context

    @property
    def request(self):
        """Gets the request of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The request of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: object
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this ODataQueryOptionsProviderListItem.


        :param request: The request of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: object
        """

        self._request = request

    @property
    def raw_values(self):
        """Gets the raw_values of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The raw_values of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: ODataRawQueryOptions
        """
        return self._raw_values

    @raw_values.setter
    def raw_values(self, raw_values):
        """Sets the raw_values of this ODataQueryOptionsProviderListItem.


        :param raw_values: The raw_values of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: ODataRawQueryOptions
        """

        self._raw_values = raw_values

    @property
    def select_expand(self):
        """Gets the select_expand of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The select_expand of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: SelectExpandQueryOption
        """
        return self._select_expand

    @select_expand.setter
    def select_expand(self, select_expand):
        """Sets the select_expand of this ODataQueryOptionsProviderListItem.


        :param select_expand: The select_expand of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: SelectExpandQueryOption
        """

        self._select_expand = select_expand

    @property
    def filter(self):
        """Gets the filter of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The filter of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: FilterQueryOption
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ODataQueryOptionsProviderListItem.


        :param filter: The filter of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: FilterQueryOption
        """

        self._filter = filter

    @property
    def order_by(self):
        """Gets the order_by of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The order_by of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: OrderByQueryOption
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ODataQueryOptionsProviderListItem.


        :param order_by: The order_by of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: OrderByQueryOption
        """

        self._order_by = order_by

    @property
    def skip(self):
        """Gets the skip of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The skip of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: SkipQueryOption
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this ODataQueryOptionsProviderListItem.


        :param skip: The skip of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: SkipQueryOption
        """

        self._skip = skip

    @property
    def top(self):
        """Gets the top of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The top of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: TopQueryOption
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this ODataQueryOptionsProviderListItem.


        :param top: The top of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: TopQueryOption
        """

        self._top = top

    @property
    def inline_count(self):
        """Gets the inline_count of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The inline_count of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: InlineCountQueryOption
        """
        return self._inline_count

    @inline_count.setter
    def inline_count(self, inline_count):
        """Sets the inline_count of this ODataQueryOptionsProviderListItem.


        :param inline_count: The inline_count of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: InlineCountQueryOption
        """

        self._inline_count = inline_count

    @property
    def validator(self):
        """Gets the validator of this ODataQueryOptionsProviderListItem.  # noqa: E501


        :return: The validator of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :rtype: ODataQueryValidator
        """
        return self._validator

    @validator.setter
    def validator(self, validator):
        """Sets the validator of this ODataQueryOptionsProviderListItem.


        :param validator: The validator of this ODataQueryOptionsProviderListItem.  # noqa: E501
        :type: ODataQueryValidator
        """

        self._validator = validator

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
        if not isinstance(other, ODataQueryOptionsProviderListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
