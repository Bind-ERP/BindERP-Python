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


class AccountingJournalItem(object):
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
        'account_id': 'str',
        'account_name': 'str',
        'description': 'str',
        'debit': 'float',
        'charge': 'float'
    }

    attribute_map = {
        'account_id': 'AccountID',
        'account_name': 'AccountName',
        'description': 'Description',
        'debit': 'Debit',
        'charge': 'Charge'
    }

    def __init__(self, account_id=None, account_name=None, description=None, debit=None, charge=None):  # noqa: E501
        """AccountingJournalItem - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._account_name = None
        self._description = None
        self._debit = None
        self._charge = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if description is not None:
            self.description = description
        if debit is not None:
            self.debit = debit
        if charge is not None:
            self.charge = charge

    @property
    def account_id(self):
        """Gets the account_id of this AccountingJournalItem.  # noqa: E501


        :return: The account_id of this AccountingJournalItem.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountingJournalItem.


        :param account_id: The account_id of this AccountingJournalItem.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_name(self):
        """Gets the account_name of this AccountingJournalItem.  # noqa: E501


        :return: The account_name of this AccountingJournalItem.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AccountingJournalItem.


        :param account_name: The account_name of this AccountingJournalItem.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def description(self):
        """Gets the description of this AccountingJournalItem.  # noqa: E501


        :return: The description of this AccountingJournalItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccountingJournalItem.


        :param description: The description of this AccountingJournalItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def debit(self):
        """Gets the debit of this AccountingJournalItem.  # noqa: E501


        :return: The debit of this AccountingJournalItem.  # noqa: E501
        :rtype: float
        """
        return self._debit

    @debit.setter
    def debit(self, debit):
        """Sets the debit of this AccountingJournalItem.


        :param debit: The debit of this AccountingJournalItem.  # noqa: E501
        :type: float
        """

        self._debit = debit

    @property
    def charge(self):
        """Gets the charge of this AccountingJournalItem.  # noqa: E501


        :return: The charge of this AccountingJournalItem.  # noqa: E501
        :rtype: float
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this AccountingJournalItem.


        :param charge: The charge of this AccountingJournalItem.  # noqa: E501
        :type: float
        """

        self._charge = charge

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
        if not isinstance(other, AccountingJournalItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
