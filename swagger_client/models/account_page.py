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

from swagger_client.models.account import Account  # noqa: F401,E501


class AccountPage(object):
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
        'value': 'list[Account]',
        'next_link': 'str',
        'count': 'int'
    }

    attribute_map = {
        'value': 'value',
        'next_link': 'nextLink',
        'count': 'count'
    }

    def __init__(self, value=None, next_link=None, count=None):  # noqa: E501
        """AccountPage - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._next_link = None
        self._count = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if next_link is not None:
            self.next_link = next_link
        if count is not None:
            self.count = count

    @property
    def value(self):
        """Gets the value of this AccountPage.  # noqa: E501


        :return: The value of this AccountPage.  # noqa: E501
        :rtype: list[Account]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AccountPage.


        :param value: The value of this AccountPage.  # noqa: E501
        :type: list[Account]
        """

        self._value = value

    @property
    def next_link(self):
        """Gets the next_link of this AccountPage.  # noqa: E501


        :return: The next_link of this AccountPage.  # noqa: E501
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this AccountPage.


        :param next_link: The next_link of this AccountPage.  # noqa: E501
        :type: str
        """

        self._next_link = next_link

    @property
    def count(self):
        """Gets the count of this AccountPage.  # noqa: E501


        :return: The count of this AccountPage.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AccountPage.


        :param count: The count of this AccountPage.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if not isinstance(other, AccountPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
