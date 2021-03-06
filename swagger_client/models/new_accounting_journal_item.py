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


class NewAccountingJournalItem(object):
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
        'sat_company_account_id': 'str',
        'cargo': 'float',
        'abono': 'float',
        'comments': 'str'
    }

    attribute_map = {
        'sat_company_account_id': 'SATCompanyAccountID',
        'cargo': 'Cargo',
        'abono': 'Abono',
        'comments': 'Comments'
    }

    def __init__(self, sat_company_account_id=None, cargo=None, abono=None, comments=None):  # noqa: E501
        """NewAccountingJournalItem - a model defined in Swagger"""  # noqa: E501

        self._sat_company_account_id = None
        self._cargo = None
        self._abono = None
        self._comments = None
        self.discriminator = None

        self.sat_company_account_id = sat_company_account_id
        self.cargo = cargo
        self.abono = abono
        if comments is not None:
            self.comments = comments

    @property
    def sat_company_account_id(self):
        """Gets the sat_company_account_id of this NewAccountingJournalItem.  # noqa: E501


        :return: The sat_company_account_id of this NewAccountingJournalItem.  # noqa: E501
        :rtype: str
        """
        return self._sat_company_account_id

    @sat_company_account_id.setter
    def sat_company_account_id(self, sat_company_account_id):
        """Sets the sat_company_account_id of this NewAccountingJournalItem.


        :param sat_company_account_id: The sat_company_account_id of this NewAccountingJournalItem.  # noqa: E501
        :type: str
        """
        if sat_company_account_id is None:
            raise ValueError("Invalid value for `sat_company_account_id`, must not be `None`")  # noqa: E501

        self._sat_company_account_id = sat_company_account_id

    @property
    def cargo(self):
        """Gets the cargo of this NewAccountingJournalItem.  # noqa: E501


        :return: The cargo of this NewAccountingJournalItem.  # noqa: E501
        :rtype: float
        """
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        """Sets the cargo of this NewAccountingJournalItem.


        :param cargo: The cargo of this NewAccountingJournalItem.  # noqa: E501
        :type: float
        """
        if cargo is None:
            raise ValueError("Invalid value for `cargo`, must not be `None`")  # noqa: E501
        if cargo is not None and cargo < 0:  # noqa: E501
            raise ValueError("Invalid value for `cargo`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cargo = cargo

    @property
    def abono(self):
        """Gets the abono of this NewAccountingJournalItem.  # noqa: E501


        :return: The abono of this NewAccountingJournalItem.  # noqa: E501
        :rtype: float
        """
        return self._abono

    @abono.setter
    def abono(self, abono):
        """Sets the abono of this NewAccountingJournalItem.


        :param abono: The abono of this NewAccountingJournalItem.  # noqa: E501
        :type: float
        """
        if abono is None:
            raise ValueError("Invalid value for `abono`, must not be `None`")  # noqa: E501
        if abono is not None and abono < 0:  # noqa: E501
            raise ValueError("Invalid value for `abono`, must be a value greater than or equal to `0`")  # noqa: E501

        self._abono = abono

    @property
    def comments(self):
        """Gets the comments of this NewAccountingJournalItem.  # noqa: E501


        :return: The comments of this NewAccountingJournalItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this NewAccountingJournalItem.


        :param comments: The comments of this NewAccountingJournalItem.  # noqa: E501
        :type: str
        """

        self._comments = comments

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
        if not isinstance(other, NewAccountingJournalItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
