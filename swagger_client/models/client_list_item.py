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


class ClientListItem(object):
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
        'number': 'int',
        'client_name': 'str',
        'legal_name': 'str',
        'rfc': 'str',
        'email': 'str',
        'phone': 'str',
        'city': 'str',
        'next_contact_date': 'datetime'
    }

    attribute_map = {
        'id': 'ID',
        'number': 'Number',
        'client_name': 'ClientName',
        'legal_name': 'LegalName',
        'rfc': 'RFC',
        'email': 'Email',
        'phone': 'Phone',
        'city': 'City',
        'next_contact_date': 'NextContactDate'
    }

    def __init__(self, id=None, number=None, client_name=None, legal_name=None, rfc=None, email=None, phone=None, city=None, next_contact_date=None):  # noqa: E501
        """ClientListItem - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._number = None
        self._client_name = None
        self._legal_name = None
        self._rfc = None
        self._email = None
        self._phone = None
        self._city = None
        self._next_contact_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if number is not None:
            self.number = number
        if client_name is not None:
            self.client_name = client_name
        if legal_name is not None:
            self.legal_name = legal_name
        if rfc is not None:
            self.rfc = rfc
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if city is not None:
            self.city = city
        if next_contact_date is not None:
            self.next_contact_date = next_contact_date

    @property
    def id(self):
        """Gets the id of this ClientListItem.  # noqa: E501


        :return: The id of this ClientListItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientListItem.


        :param id: The id of this ClientListItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def number(self):
        """Gets the number of this ClientListItem.  # noqa: E501


        :return: The number of this ClientListItem.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ClientListItem.


        :param number: The number of this ClientListItem.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def client_name(self):
        """Gets the client_name of this ClientListItem.  # noqa: E501


        :return: The client_name of this ClientListItem.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this ClientListItem.


        :param client_name: The client_name of this ClientListItem.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def legal_name(self):
        """Gets the legal_name of this ClientListItem.  # noqa: E501


        :return: The legal_name of this ClientListItem.  # noqa: E501
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """Sets the legal_name of this ClientListItem.


        :param legal_name: The legal_name of this ClientListItem.  # noqa: E501
        :type: str
        """

        self._legal_name = legal_name

    @property
    def rfc(self):
        """Gets the rfc of this ClientListItem.  # noqa: E501


        :return: The rfc of this ClientListItem.  # noqa: E501
        :rtype: str
        """
        return self._rfc

    @rfc.setter
    def rfc(self, rfc):
        """Sets the rfc of this ClientListItem.


        :param rfc: The rfc of this ClientListItem.  # noqa: E501
        :type: str
        """

        self._rfc = rfc

    @property
    def email(self):
        """Gets the email of this ClientListItem.  # noqa: E501


        :return: The email of this ClientListItem.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ClientListItem.


        :param email: The email of this ClientListItem.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this ClientListItem.  # noqa: E501


        :return: The phone of this ClientListItem.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ClientListItem.


        :param phone: The phone of this ClientListItem.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def city(self):
        """Gets the city of this ClientListItem.  # noqa: E501


        :return: The city of this ClientListItem.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ClientListItem.


        :param city: The city of this ClientListItem.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def next_contact_date(self):
        """Gets the next_contact_date of this ClientListItem.  # noqa: E501


        :return: The next_contact_date of this ClientListItem.  # noqa: E501
        :rtype: datetime
        """
        return self._next_contact_date

    @next_contact_date.setter
    def next_contact_date(self, next_contact_date):
        """Sets the next_contact_date of this ClientListItem.


        :param next_contact_date: The next_contact_date of this ClientListItem.  # noqa: E501
        :type: datetime
        """

        self._next_contact_date = next_contact_date

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
        if not isinstance(other, ClientListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other