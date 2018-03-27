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

from swagger_client.models.select_item import SelectItem  # noqa: F401,E501


class SelectExpandClause(object):
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
        'selected_items': 'list[SelectItem]',
        'all_selected': 'bool'
    }

    attribute_map = {
        'selected_items': 'SelectedItems',
        'all_selected': 'AllSelected'
    }

    def __init__(self, selected_items=None, all_selected=None):  # noqa: E501
        """SelectExpandClause - a model defined in Swagger"""  # noqa: E501

        self._selected_items = None
        self._all_selected = None
        self.discriminator = None

        if selected_items is not None:
            self.selected_items = selected_items
        if all_selected is not None:
            self.all_selected = all_selected

    @property
    def selected_items(self):
        """Gets the selected_items of this SelectExpandClause.  # noqa: E501


        :return: The selected_items of this SelectExpandClause.  # noqa: E501
        :rtype: list[SelectItem]
        """
        return self._selected_items

    @selected_items.setter
    def selected_items(self, selected_items):
        """Sets the selected_items of this SelectExpandClause.


        :param selected_items: The selected_items of this SelectExpandClause.  # noqa: E501
        :type: list[SelectItem]
        """

        self._selected_items = selected_items

    @property
    def all_selected(self):
        """Gets the all_selected of this SelectExpandClause.  # noqa: E501


        :return: The all_selected of this SelectExpandClause.  # noqa: E501
        :rtype: bool
        """
        return self._all_selected

    @all_selected.setter
    def all_selected(self, all_selected):
        """Sets the all_selected of this SelectExpandClause.


        :param all_selected: The all_selected of this SelectExpandClause.  # noqa: E501
        :type: bool
        """

        self._all_selected = all_selected

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
        if not isinstance(other, SelectExpandClause):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
