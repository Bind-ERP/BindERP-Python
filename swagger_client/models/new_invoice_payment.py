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


class NewInvoicePayment(object):
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
        'payment_method': 'int',
        'account_id': 'str',
        'amount': 'float',
        'exchange_rate': 'float',
        'exchange_rate_account': 'float',
        'reference': 'str'
    }

    attribute_map = {
        'payment_method': 'PaymentMethod',
        'account_id': 'AccountID',
        'amount': 'Amount',
        'exchange_rate': 'ExchangeRate',
        'exchange_rate_account': 'ExchangeRateAccount',
        'reference': 'Reference'
    }

    def __init__(self, payment_method=None, account_id=None, amount=None, exchange_rate=None, exchange_rate_account=None, reference=None):  # noqa: E501
        """NewInvoicePayment - a model defined in Swagger"""  # noqa: E501

        self._payment_method = None
        self._account_id = None
        self._amount = None
        self._exchange_rate = None
        self._exchange_rate_account = None
        self._reference = None
        self.discriminator = None

        self.payment_method = payment_method
        self.account_id = account_id
        self.amount = amount
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if exchange_rate_account is not None:
            self.exchange_rate_account = exchange_rate_account
        self.reference = reference

    @property
    def payment_method(self):
        """Gets the payment_method of this NewInvoicePayment.  # noqa: E501


        :return: The payment_method of this NewInvoicePayment.  # noqa: E501
        :rtype: int
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this NewInvoicePayment.


        :param payment_method: The payment_method of this NewInvoicePayment.  # noqa: E501
        :type: int
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def account_id(self):
        """Gets the account_id of this NewInvoicePayment.  # noqa: E501


        :return: The account_id of this NewInvoicePayment.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this NewInvoicePayment.


        :param account_id: The account_id of this NewInvoicePayment.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def amount(self):
        """Gets the amount of this NewInvoicePayment.  # noqa: E501


        :return: The amount of this NewInvoicePayment.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this NewInvoicePayment.


        :param amount: The amount of this NewInvoicePayment.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this NewInvoicePayment.  # noqa: E501


        :return: The exchange_rate of this NewInvoicePayment.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this NewInvoicePayment.


        :param exchange_rate: The exchange_rate of this NewInvoicePayment.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def exchange_rate_account(self):
        """Gets the exchange_rate_account of this NewInvoicePayment.  # noqa: E501


        :return: The exchange_rate_account of this NewInvoicePayment.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate_account

    @exchange_rate_account.setter
    def exchange_rate_account(self, exchange_rate_account):
        """Sets the exchange_rate_account of this NewInvoicePayment.


        :param exchange_rate_account: The exchange_rate_account of this NewInvoicePayment.  # noqa: E501
        :type: float
        """

        self._exchange_rate_account = exchange_rate_account

    @property
    def reference(self):
        """Gets the reference of this NewInvoicePayment.  # noqa: E501


        :return: The reference of this NewInvoicePayment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this NewInvoicePayment.


        :param reference: The reference of this NewInvoicePayment.  # noqa: E501
        :type: str
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

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
        if not isinstance(other, NewInvoicePayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other