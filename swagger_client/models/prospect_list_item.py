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


class ProspectListItem(object):
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
        'company_name': 'str',
        'prospect_name': 'str',
        'email': 'str',
        'phone': 'str',
        'id': 'str',
        'sales_man': 'str'
    }

    attribute_map = {
        'company_name': 'CompanyName',
        'prospect_name': 'ProspectName',
        'email': 'Email',
        'phone': 'Phone',
        'id': 'ID',
        'sales_man': 'SalesMan'
    }

    def __init__(self, company_name=None, prospect_name=None, email=None, phone=None, id=None, sales_man=None):  # noqa: E501
        """ProspectListItem - a model defined in Swagger"""  # noqa: E501

        self._company_name = None
        self._prospect_name = None
        self._email = None
        self._phone = None
        self._id = None
        self._sales_man = None
        self.discriminator = None

        if company_name is not None:
            self.company_name = company_name
        if prospect_name is not None:
            self.prospect_name = prospect_name
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if id is not None:
            self.id = id
        if sales_man is not None:
            self.sales_man = sales_man

    @property
    def company_name(self):
        """Gets the company_name of this ProspectListItem.  # noqa: E501


        :return: The company_name of this ProspectListItem.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ProspectListItem.


        :param company_name: The company_name of this ProspectListItem.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def prospect_name(self):
        """Gets the prospect_name of this ProspectListItem.  # noqa: E501


        :return: The prospect_name of this ProspectListItem.  # noqa: E501
        :rtype: str
        """
        return self._prospect_name

    @prospect_name.setter
    def prospect_name(self, prospect_name):
        """Sets the prospect_name of this ProspectListItem.


        :param prospect_name: The prospect_name of this ProspectListItem.  # noqa: E501
        :type: str
        """

        self._prospect_name = prospect_name

    @property
    def email(self):
        """Gets the email of this ProspectListItem.  # noqa: E501


        :return: The email of this ProspectListItem.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ProspectListItem.


        :param email: The email of this ProspectListItem.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this ProspectListItem.  # noqa: E501


        :return: The phone of this ProspectListItem.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ProspectListItem.


        :param phone: The phone of this ProspectListItem.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def id(self):
        """Gets the id of this ProspectListItem.  # noqa: E501


        :return: The id of this ProspectListItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProspectListItem.


        :param id: The id of this ProspectListItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sales_man(self):
        """Gets the sales_man of this ProspectListItem.  # noqa: E501


        :return: The sales_man of this ProspectListItem.  # noqa: E501
        :rtype: str
        """
        return self._sales_man

    @sales_man.setter
    def sales_man(self, sales_man):
        """Sets the sales_man of this ProspectListItem.


        :param sales_man: The sales_man of this ProspectListItem.  # noqa: E501
        :type: str
        """

        self._sales_man = sales_man

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
        if not isinstance(other, ProspectListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other