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


class NewInventoryAdjustment(object):
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
        'product_id': 'str',
        'warehouse_id': 'str',
        'lot_import_id': 'str',
        'adjust_qty': 'float',
        'date': 'str',
        'comments': 'str',
        'accounting_account_id': 'str'
    }

    attribute_map = {
        'product_id': 'ProductID',
        'warehouse_id': 'WarehouseID',
        'lot_import_id': 'LotImportID',
        'adjust_qty': 'AdjustQty',
        'date': 'Date',
        'comments': 'Comments',
        'accounting_account_id': 'AccountingAccountID'
    }

    def __init__(self, product_id=None, warehouse_id=None, lot_import_id=None, adjust_qty=None, date=None, comments=None, accounting_account_id=None):  # noqa: E501
        """NewInventoryAdjustment - a model defined in Swagger"""  # noqa: E501

        self._product_id = None
        self._warehouse_id = None
        self._lot_import_id = None
        self._adjust_qty = None
        self._date = None
        self._comments = None
        self._accounting_account_id = None
        self.discriminator = None

        self.product_id = product_id
        self.warehouse_id = warehouse_id
        if lot_import_id is not None:
            self.lot_import_id = lot_import_id
        self.adjust_qty = adjust_qty
        self.date = date
        self.comments = comments
        if accounting_account_id is not None:
            self.accounting_account_id = accounting_account_id

    @property
    def product_id(self):
        """Gets the product_id of this NewInventoryAdjustment.  # noqa: E501


        :return: The product_id of this NewInventoryAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this NewInventoryAdjustment.


        :param product_id: The product_id of this NewInventoryAdjustment.  # noqa: E501
        :type: str
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this NewInventoryAdjustment.  # noqa: E501


        :return: The warehouse_id of this NewInventoryAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this NewInventoryAdjustment.


        :param warehouse_id: The warehouse_id of this NewInventoryAdjustment.  # noqa: E501
        :type: str
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def lot_import_id(self):
        """Gets the lot_import_id of this NewInventoryAdjustment.  # noqa: E501


        :return: The lot_import_id of this NewInventoryAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._lot_import_id

    @lot_import_id.setter
    def lot_import_id(self, lot_import_id):
        """Sets the lot_import_id of this NewInventoryAdjustment.


        :param lot_import_id: The lot_import_id of this NewInventoryAdjustment.  # noqa: E501
        :type: str
        """

        self._lot_import_id = lot_import_id

    @property
    def adjust_qty(self):
        """Gets the adjust_qty of this NewInventoryAdjustment.  # noqa: E501


        :return: The adjust_qty of this NewInventoryAdjustment.  # noqa: E501
        :rtype: float
        """
        return self._adjust_qty

    @adjust_qty.setter
    def adjust_qty(self, adjust_qty):
        """Sets the adjust_qty of this NewInventoryAdjustment.


        :param adjust_qty: The adjust_qty of this NewInventoryAdjustment.  # noqa: E501
        :type: float
        """
        if adjust_qty is None:
            raise ValueError("Invalid value for `adjust_qty`, must not be `None`")  # noqa: E501

        self._adjust_qty = adjust_qty

    @property
    def date(self):
        """Gets the date of this NewInventoryAdjustment.  # noqa: E501


        :return: The date of this NewInventoryAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this NewInventoryAdjustment.


        :param date: The date of this NewInventoryAdjustment.  # noqa: E501
        :type: str
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def comments(self):
        """Gets the comments of this NewInventoryAdjustment.  # noqa: E501


        :return: The comments of this NewInventoryAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this NewInventoryAdjustment.


        :param comments: The comments of this NewInventoryAdjustment.  # noqa: E501
        :type: str
        """
        if comments is None:
            raise ValueError("Invalid value for `comments`, must not be `None`")  # noqa: E501

        self._comments = comments

    @property
    def accounting_account_id(self):
        """Gets the accounting_account_id of this NewInventoryAdjustment.  # noqa: E501


        :return: The accounting_account_id of this NewInventoryAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._accounting_account_id

    @accounting_account_id.setter
    def accounting_account_id(self, accounting_account_id):
        """Sets the accounting_account_id of this NewInventoryAdjustment.


        :param accounting_account_id: The accounting_account_id of this NewInventoryAdjustment.  # noqa: E501
        :type: str
        """

        self._accounting_account_id = accounting_account_id

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
        if not isinstance(other, NewInventoryAdjustment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
