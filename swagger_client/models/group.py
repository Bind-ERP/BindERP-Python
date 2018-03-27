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

from swagger_client.models.sub_groups import SubGroups  # noqa: F401,E501


class Group(object):
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
        'id': 'str',
        'code': 'str',
        'prefix': 'str',
        'description': 'str',
        'sub_groups': 'list[SubGroups]'
    }

    attribute_map = {
        'id': 'ID',
        'code': 'Code',
        'prefix': 'Prefix',
        'description': 'Description',
        'sub_groups': 'SubGroups'
    }

    def __init__(self, id=None, code=None, prefix=None, description=None, sub_groups=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._code = None
        self._prefix = None
        self._description = None
        self._sub_groups = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if prefix is not None:
            self.prefix = prefix
        if description is not None:
            self.description = description
        if sub_groups is not None:
            self.sub_groups = sub_groups

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501


        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.


        :param id: The id of this Group.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this Group.  # noqa: E501


        :return: The code of this Group.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Group.


        :param code: The code of this Group.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def prefix(self):
        """Gets the prefix of this Group.  # noqa: E501


        :return: The prefix of this Group.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this Group.


        :param prefix: The prefix of this Group.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def description(self):
        """Gets the description of this Group.  # noqa: E501


        :return: The description of this Group.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Group.


        :param description: The description of this Group.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def sub_groups(self):
        """Gets the sub_groups of this Group.  # noqa: E501


        :return: The sub_groups of this Group.  # noqa: E501
        :rtype: list[SubGroups]
        """
        return self._sub_groups

    @sub_groups.setter
    def sub_groups(self, sub_groups):
        """Sets the sub_groups of this Group.


        :param sub_groups: The sub_groups of this Group.  # noqa: E501
        :type: list[SubGroups]
        """

        self._sub_groups = sub_groups

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
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
