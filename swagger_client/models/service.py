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


class Service(object):
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
        'description': 'str',
        'creation_date': 'datetime',
        'category1_id': 'str',
        'category2_id': 'str',
        'category3_id': 'str',
        'charge_vat': 'bool',
        'pricing_type': 'int',
        'pricing_type_text': 'str',
        'unit': 'str',
        'currency_id': 'str',
        'currency_code': 'str',
        'variable_concept': 'bool',
        'sat_code': 'int',
        'sat_unit': 'int'
    }

    attribute_map = {
        'id': 'ID',
        'code': 'Code',
        'title': 'Title',
        'description': 'Description',
        'creation_date': 'CreationDate',
        'category1_id': 'Category1ID',
        'category2_id': 'Category2ID',
        'category3_id': 'Category3ID',
        'charge_vat': 'ChargeVAT',
        'pricing_type': 'PricingType',
        'pricing_type_text': 'PricingTypeText',
        'unit': 'Unit',
        'currency_id': 'CurrencyID',
        'currency_code': 'CurrencyCode',
        'variable_concept': 'VariableConcept',
        'sat_code': 'SATCode',
        'sat_unit': 'SATUnit'
    }

    def __init__(self, id=None, code=None, title=None, description=None, creation_date=None, category1_id=None, category2_id=None, category3_id=None, charge_vat=None, pricing_type=None, pricing_type_text=None, unit=None, currency_id=None, currency_code=None, variable_concept=None, sat_code=None, sat_unit=None):  # noqa: E501
        """Service - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._code = None
        self._title = None
        self._description = None
        self._creation_date = None
        self._category1_id = None
        self._category2_id = None
        self._category3_id = None
        self._charge_vat = None
        self._pricing_type = None
        self._pricing_type_text = None
        self._unit = None
        self._currency_id = None
        self._currency_code = None
        self._variable_concept = None
        self._sat_code = None
        self._sat_unit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if creation_date is not None:
            self.creation_date = creation_date
        if category1_id is not None:
            self.category1_id = category1_id
        if category2_id is not None:
            self.category2_id = category2_id
        if category3_id is not None:
            self.category3_id = category3_id
        if charge_vat is not None:
            self.charge_vat = charge_vat
        if pricing_type is not None:
            self.pricing_type = pricing_type
        if pricing_type_text is not None:
            self.pricing_type_text = pricing_type_text
        if unit is not None:
            self.unit = unit
        if currency_id is not None:
            self.currency_id = currency_id
        if currency_code is not None:
            self.currency_code = currency_code
        if variable_concept is not None:
            self.variable_concept = variable_concept
        if sat_code is not None:
            self.sat_code = sat_code
        if sat_unit is not None:
            self.sat_unit = sat_unit

    @property
    def id(self):
        """Gets the id of this Service.  # noqa: E501


        :return: The id of this Service.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Service.


        :param id: The id of this Service.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this Service.  # noqa: E501


        :return: The code of this Service.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Service.


        :param code: The code of this Service.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def title(self):
        """Gets the title of this Service.  # noqa: E501


        :return: The title of this Service.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Service.


        :param title: The title of this Service.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this Service.  # noqa: E501


        :return: The description of this Service.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Service.


        :param description: The description of this Service.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def creation_date(self):
        """Gets the creation_date of this Service.  # noqa: E501


        :return: The creation_date of this Service.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Service.


        :param creation_date: The creation_date of this Service.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def category1_id(self):
        """Gets the category1_id of this Service.  # noqa: E501


        :return: The category1_id of this Service.  # noqa: E501
        :rtype: str
        """
        return self._category1_id

    @category1_id.setter
    def category1_id(self, category1_id):
        """Sets the category1_id of this Service.


        :param category1_id: The category1_id of this Service.  # noqa: E501
        :type: str
        """

        self._category1_id = category1_id

    @property
    def category2_id(self):
        """Gets the category2_id of this Service.  # noqa: E501


        :return: The category2_id of this Service.  # noqa: E501
        :rtype: str
        """
        return self._category2_id

    @category2_id.setter
    def category2_id(self, category2_id):
        """Sets the category2_id of this Service.


        :param category2_id: The category2_id of this Service.  # noqa: E501
        :type: str
        """

        self._category2_id = category2_id

    @property
    def category3_id(self):
        """Gets the category3_id of this Service.  # noqa: E501


        :return: The category3_id of this Service.  # noqa: E501
        :rtype: str
        """
        return self._category3_id

    @category3_id.setter
    def category3_id(self, category3_id):
        """Sets the category3_id of this Service.


        :param category3_id: The category3_id of this Service.  # noqa: E501
        :type: str
        """

        self._category3_id = category3_id

    @property
    def charge_vat(self):
        """Gets the charge_vat of this Service.  # noqa: E501


        :return: The charge_vat of this Service.  # noqa: E501
        :rtype: bool
        """
        return self._charge_vat

    @charge_vat.setter
    def charge_vat(self, charge_vat):
        """Sets the charge_vat of this Service.


        :param charge_vat: The charge_vat of this Service.  # noqa: E501
        :type: bool
        """

        self._charge_vat = charge_vat

    @property
    def pricing_type(self):
        """Gets the pricing_type of this Service.  # noqa: E501


        :return: The pricing_type of this Service.  # noqa: E501
        :rtype: int
        """
        return self._pricing_type

    @pricing_type.setter
    def pricing_type(self, pricing_type):
        """Sets the pricing_type of this Service.


        :param pricing_type: The pricing_type of this Service.  # noqa: E501
        :type: int
        """

        self._pricing_type = pricing_type

    @property
    def pricing_type_text(self):
        """Gets the pricing_type_text of this Service.  # noqa: E501


        :return: The pricing_type_text of this Service.  # noqa: E501
        :rtype: str
        """
        return self._pricing_type_text

    @pricing_type_text.setter
    def pricing_type_text(self, pricing_type_text):
        """Sets the pricing_type_text of this Service.


        :param pricing_type_text: The pricing_type_text of this Service.  # noqa: E501
        :type: str
        """

        self._pricing_type_text = pricing_type_text

    @property
    def unit(self):
        """Gets the unit of this Service.  # noqa: E501


        :return: The unit of this Service.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Service.


        :param unit: The unit of this Service.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def currency_id(self):
        """Gets the currency_id of this Service.  # noqa: E501


        :return: The currency_id of this Service.  # noqa: E501
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this Service.


        :param currency_id: The currency_id of this Service.  # noqa: E501
        :type: str
        """

        self._currency_id = currency_id

    @property
    def currency_code(self):
        """Gets the currency_code of this Service.  # noqa: E501


        :return: The currency_code of this Service.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Service.


        :param currency_code: The currency_code of this Service.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def variable_concept(self):
        """Gets the variable_concept of this Service.  # noqa: E501


        :return: The variable_concept of this Service.  # noqa: E501
        :rtype: bool
        """
        return self._variable_concept

    @variable_concept.setter
    def variable_concept(self, variable_concept):
        """Sets the variable_concept of this Service.


        :param variable_concept: The variable_concept of this Service.  # noqa: E501
        :type: bool
        """

        self._variable_concept = variable_concept

    @property
    def sat_code(self):
        """Gets the sat_code of this Service.  # noqa: E501


        :return: The sat_code of this Service.  # noqa: E501
        :rtype: int
        """
        return self._sat_code

    @sat_code.setter
    def sat_code(self, sat_code):
        """Sets the sat_code of this Service.


        :param sat_code: The sat_code of this Service.  # noqa: E501
        :type: int
        """

        self._sat_code = sat_code

    @property
    def sat_unit(self):
        """Gets the sat_unit of this Service.  # noqa: E501


        :return: The sat_unit of this Service.  # noqa: E501
        :rtype: int
        """
        return self._sat_unit

    @sat_unit.setter
    def sat_unit(self, sat_unit):
        """Sets the sat_unit of this Service.


        :param sat_unit: The sat_unit of this Service.  # noqa: E501
        :type: int
        """

        self._sat_unit = sat_unit

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
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
