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


class Series(object):
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
        'serie': 'str',
        'start_number': 'int',
        'current_number': 'int',
        'date': 'datetime',
        'doc_type': 'int',
        'doc_type_text': 'str',
        'locations': 'list[str]'
    }

    attribute_map = {
        'id': 'ID',
        'serie': 'Serie',
        'start_number': 'StartNumber',
        'current_number': 'CurrentNumber',
        'date': 'Date',
        'doc_type': 'DocType',
        'doc_type_text': 'DocTypeText',
        'locations': 'Locations'
    }

    def __init__(self, id=None, serie=None, start_number=None, current_number=None, date=None, doc_type=None, doc_type_text=None, locations=None):  # noqa: E501
        """Series - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._serie = None
        self._start_number = None
        self._current_number = None
        self._date = None
        self._doc_type = None
        self._doc_type_text = None
        self._locations = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if serie is not None:
            self.serie = serie
        if start_number is not None:
            self.start_number = start_number
        if current_number is not None:
            self.current_number = current_number
        if date is not None:
            self.date = date
        if doc_type is not None:
            self.doc_type = doc_type
        if doc_type_text is not None:
            self.doc_type_text = doc_type_text
        if locations is not None:
            self.locations = locations

    @property
    def id(self):
        """Gets the id of this Series.  # noqa: E501


        :return: The id of this Series.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Series.


        :param id: The id of this Series.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def serie(self):
        """Gets the serie of this Series.  # noqa: E501


        :return: The serie of this Series.  # noqa: E501
        :rtype: str
        """
        return self._serie

    @serie.setter
    def serie(self, serie):
        """Sets the serie of this Series.


        :param serie: The serie of this Series.  # noqa: E501
        :type: str
        """

        self._serie = serie

    @property
    def start_number(self):
        """Gets the start_number of this Series.  # noqa: E501


        :return: The start_number of this Series.  # noqa: E501
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this Series.


        :param start_number: The start_number of this Series.  # noqa: E501
        :type: int
        """

        self._start_number = start_number

    @property
    def current_number(self):
        """Gets the current_number of this Series.  # noqa: E501


        :return: The current_number of this Series.  # noqa: E501
        :rtype: int
        """
        return self._current_number

    @current_number.setter
    def current_number(self, current_number):
        """Sets the current_number of this Series.


        :param current_number: The current_number of this Series.  # noqa: E501
        :type: int
        """

        self._current_number = current_number

    @property
    def date(self):
        """Gets the date of this Series.  # noqa: E501


        :return: The date of this Series.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Series.


        :param date: The date of this Series.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def doc_type(self):
        """Gets the doc_type of this Series.  # noqa: E501


        :return: The doc_type of this Series.  # noqa: E501
        :rtype: int
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        """Sets the doc_type of this Series.


        :param doc_type: The doc_type of this Series.  # noqa: E501
        :type: int
        """

        self._doc_type = doc_type

    @property
    def doc_type_text(self):
        """Gets the doc_type_text of this Series.  # noqa: E501


        :return: The doc_type_text of this Series.  # noqa: E501
        :rtype: str
        """
        return self._doc_type_text

    @doc_type_text.setter
    def doc_type_text(self, doc_type_text):
        """Sets the doc_type_text of this Series.


        :param doc_type_text: The doc_type_text of this Series.  # noqa: E501
        :type: str
        """

        self._doc_type_text = doc_type_text

    @property
    def locations(self):
        """Gets the locations of this Series.  # noqa: E501


        :return: The locations of this Series.  # noqa: E501
        :rtype: list[str]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this Series.


        :param locations: The locations of this Series.  # noqa: E501
        :type: list[str]
        """

        self._locations = locations

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
        if not isinstance(other, Series):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other