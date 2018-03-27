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


class EditService(object):
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
        'title': 'str',
        'currency_id': 'str',
        'sat_company_account_id': 'str',
        'measurement_unit': 'str',
        'description': 'str',
        'category1_id': 'str',
        'category2_id': 'str',
        'category3_id': 'str',
        'variable_concept': 'bool',
        'charge_vat': 'bool'
    }

    attribute_map = {
        'id': 'ID',
        'code': 'Code',
        'title': 'Title',
        'currency_id': 'CurrencyID',
        'sat_company_account_id': 'SATCompanyAccountID',
        'measurement_unit': 'MeasurementUnit',
        'description': 'Description',
        'category1_id': 'Category1ID',
        'category2_id': 'Category2ID',
        'category3_id': 'Category3ID',
        'variable_concept': 'VariableConcept',
        'charge_vat': 'ChargeVAT'
    }

    def __init__(self, id=None, code=None, title=None, currency_id=None, sat_company_account_id=None, measurement_unit=None, description=None, category1_id=None, category2_id=None, category3_id=None, variable_concept=None, charge_vat=None):  # noqa: E501
        """EditService - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._code = None
        self._title = None
        self._currency_id = None
        self._sat_company_account_id = None
        self._measurement_unit = None
        self._description = None
        self._category1_id = None
        self._category2_id = None
        self._category3_id = None
        self._variable_concept = None
        self._charge_vat = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if title is not None:
            self.title = title
        if currency_id is not None:
            self.currency_id = currency_id
        if sat_company_account_id is not None:
            self.sat_company_account_id = sat_company_account_id
        if measurement_unit is not None:
            self.measurement_unit = measurement_unit
        if description is not None:
            self.description = description
        if category1_id is not None:
            self.category1_id = category1_id
        if category2_id is not None:
            self.category2_id = category2_id
        if category3_id is not None:
            self.category3_id = category3_id
        if variable_concept is not None:
            self.variable_concept = variable_concept
        if charge_vat is not None:
            self.charge_vat = charge_vat

    @property
    def id(self):
        """Gets the id of this EditService.  # noqa: E501


        :return: The id of this EditService.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EditService.


        :param id: The id of this EditService.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this EditService.  # noqa: E501


        :return: The code of this EditService.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EditService.


        :param code: The code of this EditService.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def title(self):
        """Gets the title of this EditService.  # noqa: E501


        :return: The title of this EditService.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EditService.


        :param title: The title of this EditService.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def currency_id(self):
        """Gets the currency_id of this EditService.  # noqa: E501


        :return: The currency_id of this EditService.  # noqa: E501
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this EditService.


        :param currency_id: The currency_id of this EditService.  # noqa: E501
        :type: str
        """

        self._currency_id = currency_id

    @property
    def sat_company_account_id(self):
        """Gets the sat_company_account_id of this EditService.  # noqa: E501


        :return: The sat_company_account_id of this EditService.  # noqa: E501
        :rtype: str
        """
        return self._sat_company_account_id

    @sat_company_account_id.setter
    def sat_company_account_id(self, sat_company_account_id):
        """Sets the sat_company_account_id of this EditService.


        :param sat_company_account_id: The sat_company_account_id of this EditService.  # noqa: E501
        :type: str
        """

        self._sat_company_account_id = sat_company_account_id

    @property
    def measurement_unit(self):
        """Gets the measurement_unit of this EditService.  # noqa: E501


        :return: The measurement_unit of this EditService.  # noqa: E501
        :rtype: str
        """
        return self._measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, measurement_unit):
        """Sets the measurement_unit of this EditService.


        :param measurement_unit: The measurement_unit of this EditService.  # noqa: E501
        :type: str
        """

        self._measurement_unit = measurement_unit

    @property
    def description(self):
        """Gets the description of this EditService.  # noqa: E501


        :return: The description of this EditService.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EditService.


        :param description: The description of this EditService.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def category1_id(self):
        """Gets the category1_id of this EditService.  # noqa: E501


        :return: The category1_id of this EditService.  # noqa: E501
        :rtype: str
        """
        return self._category1_id

    @category1_id.setter
    def category1_id(self, category1_id):
        """Sets the category1_id of this EditService.


        :param category1_id: The category1_id of this EditService.  # noqa: E501
        :type: str
        """

        self._category1_id = category1_id

    @property
    def category2_id(self):
        """Gets the category2_id of this EditService.  # noqa: E501


        :return: The category2_id of this EditService.  # noqa: E501
        :rtype: str
        """
        return self._category2_id

    @category2_id.setter
    def category2_id(self, category2_id):
        """Sets the category2_id of this EditService.


        :param category2_id: The category2_id of this EditService.  # noqa: E501
        :type: str
        """

        self._category2_id = category2_id

    @property
    def category3_id(self):
        """Gets the category3_id of this EditService.  # noqa: E501


        :return: The category3_id of this EditService.  # noqa: E501
        :rtype: str
        """
        return self._category3_id

    @category3_id.setter
    def category3_id(self, category3_id):
        """Sets the category3_id of this EditService.


        :param category3_id: The category3_id of this EditService.  # noqa: E501
        :type: str
        """

        self._category3_id = category3_id

    @property
    def variable_concept(self):
        """Gets the variable_concept of this EditService.  # noqa: E501


        :return: The variable_concept of this EditService.  # noqa: E501
        :rtype: bool
        """
        return self._variable_concept

    @variable_concept.setter
    def variable_concept(self, variable_concept):
        """Sets the variable_concept of this EditService.


        :param variable_concept: The variable_concept of this EditService.  # noqa: E501
        :type: bool
        """

        self._variable_concept = variable_concept

    @property
    def charge_vat(self):
        """Gets the charge_vat of this EditService.  # noqa: E501


        :return: The charge_vat of this EditService.  # noqa: E501
        :rtype: bool
        """
        return self._charge_vat

    @charge_vat.setter
    def charge_vat(self, charge_vat):
        """Sets the charge_vat of this EditService.


        :param charge_vat: The charge_vat of this EditService.  # noqa: E501
        :type: bool
        """

        self._charge_vat = charge_vat

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
        if not isinstance(other, EditService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
