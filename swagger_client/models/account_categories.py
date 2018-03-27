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

from swagger_client.models.gl_group import GLGroup  # noqa: F401,E501


class AccountCategories(object):
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
        'gl_groups': 'list[GLGroup]'
    }

    attribute_map = {
        'gl_groups': 'GLGroups'
    }

    def __init__(self, gl_groups=None):  # noqa: E501
        """AccountCategories - a model defined in Swagger"""  # noqa: E501

        self._gl_groups = None
        self.discriminator = None

        if gl_groups is not None:
            self.gl_groups = gl_groups

    @property
    def gl_groups(self):
        """Gets the gl_groups of this AccountCategories.  # noqa: E501


        :return: The gl_groups of this AccountCategories.  # noqa: E501
        :rtype: list[GLGroup]
        """
        return self._gl_groups

    @gl_groups.setter
    def gl_groups(self, gl_groups):
        """Sets the gl_groups of this AccountCategories.


        :param gl_groups: The gl_groups of this AccountCategories.  # noqa: E501
        :type: list[GLGroup]
        """

        self._gl_groups = gl_groups

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
        if not isinstance(other, AccountCategories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
