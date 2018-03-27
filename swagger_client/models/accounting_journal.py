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

from swagger_client.models.accounting_journal_item import AccountingJournalItem  # noqa: F401,E501


class AccountingJournal(object):
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
        'document_id': 'str',
        'type': 'str',
        'application_date': 'datetime',
        'creation_date': 'datetime',
        'number': 'int',
        'location_id': 'str',
        'period_type': 'str',
        'items': 'list[AccountingJournalItem]'
    }

    attribute_map = {
        'id': 'ID',
        'document_id': 'DocumentID',
        'type': 'Type',
        'application_date': 'ApplicationDate',
        'creation_date': 'CreationDate',
        'number': 'Number',
        'location_id': 'LocationID',
        'period_type': 'PeriodType',
        'items': 'Items'
    }

    def __init__(self, id=None, document_id=None, type=None, application_date=None, creation_date=None, number=None, location_id=None, period_type=None, items=None):  # noqa: E501
        """AccountingJournal - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._document_id = None
        self._type = None
        self._application_date = None
        self._creation_date = None
        self._number = None
        self._location_id = None
        self._period_type = None
        self._items = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if document_id is not None:
            self.document_id = document_id
        if type is not None:
            self.type = type
        if application_date is not None:
            self.application_date = application_date
        if creation_date is not None:
            self.creation_date = creation_date
        if number is not None:
            self.number = number
        if location_id is not None:
            self.location_id = location_id
        if period_type is not None:
            self.period_type = period_type
        if items is not None:
            self.items = items

    @property
    def id(self):
        """Gets the id of this AccountingJournal.  # noqa: E501


        :return: The id of this AccountingJournal.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountingJournal.


        :param id: The id of this AccountingJournal.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def document_id(self):
        """Gets the document_id of this AccountingJournal.  # noqa: E501


        :return: The document_id of this AccountingJournal.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this AccountingJournal.


        :param document_id: The document_id of this AccountingJournal.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def type(self):
        """Gets the type of this AccountingJournal.  # noqa: E501


        :return: The type of this AccountingJournal.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountingJournal.


        :param type: The type of this AccountingJournal.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def application_date(self):
        """Gets the application_date of this AccountingJournal.  # noqa: E501


        :return: The application_date of this AccountingJournal.  # noqa: E501
        :rtype: datetime
        """
        return self._application_date

    @application_date.setter
    def application_date(self, application_date):
        """Sets the application_date of this AccountingJournal.


        :param application_date: The application_date of this AccountingJournal.  # noqa: E501
        :type: datetime
        """

        self._application_date = application_date

    @property
    def creation_date(self):
        """Gets the creation_date of this AccountingJournal.  # noqa: E501


        :return: The creation_date of this AccountingJournal.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this AccountingJournal.


        :param creation_date: The creation_date of this AccountingJournal.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def number(self):
        """Gets the number of this AccountingJournal.  # noqa: E501


        :return: The number of this AccountingJournal.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this AccountingJournal.


        :param number: The number of this AccountingJournal.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def location_id(self):
        """Gets the location_id of this AccountingJournal.  # noqa: E501


        :return: The location_id of this AccountingJournal.  # noqa: E501
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this AccountingJournal.


        :param location_id: The location_id of this AccountingJournal.  # noqa: E501
        :type: str
        """

        self._location_id = location_id

    @property
    def period_type(self):
        """Gets the period_type of this AccountingJournal.  # noqa: E501


        :return: The period_type of this AccountingJournal.  # noqa: E501
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this AccountingJournal.


        :param period_type: The period_type of this AccountingJournal.  # noqa: E501
        :type: str
        """

        self._period_type = period_type

    @property
    def items(self):
        """Gets the items of this AccountingJournal.  # noqa: E501


        :return: The items of this AccountingJournal.  # noqa: E501
        :rtype: list[AccountingJournalItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this AccountingJournal.


        :param items: The items of this AccountingJournal.  # noqa: E501
        :type: list[AccountingJournalItem]
        """

        self._items = items

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
        if not isinstance(other, AccountingJournal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other