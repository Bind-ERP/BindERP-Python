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


class NewActivity(object):
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
        'comment': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'event_type': 'str',
        'is_public': 'bool',
        'title': 'str',
        'repeatable': 'bool',
        'repeat_interval': 'int',
        'repeat_type': 'int',
        'repetitions': 'int',
        'external_id': 'str',
        'external_id_type': 'int'
    }

    attribute_map = {
        'comment': 'Comment',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'event_type': 'EventType',
        'is_public': 'IsPublic',
        'title': 'Title',
        'repeatable': 'Repeatable',
        'repeat_interval': 'RepeatInterval',
        'repeat_type': 'RepeatType',
        'repetitions': 'Repetitions',
        'external_id': 'ExternalID',
        'external_id_type': 'ExternalIDType'
    }

    def __init__(self, comment=None, start_date=None, end_date=None, event_type=None, is_public=None, title=None, repeatable=None, repeat_interval=None, repeat_type=None, repetitions=None, external_id=None, external_id_type=None):  # noqa: E501
        """NewActivity - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._start_date = None
        self._end_date = None
        self._event_type = None
        self._is_public = None
        self._title = None
        self._repeatable = None
        self._repeat_interval = None
        self._repeat_type = None
        self._repetitions = None
        self._external_id = None
        self._external_id_type = None
        self.discriminator = None

        self.comment = comment
        self.start_date = start_date
        self.end_date = end_date
        self.event_type = event_type
        self.is_public = is_public
        self.title = title
        self.repeatable = repeatable
        if repeat_interval is not None:
            self.repeat_interval = repeat_interval
        if repeat_type is not None:
            self.repeat_type = repeat_type
        if repetitions is not None:
            self.repetitions = repetitions
        if external_id is not None:
            self.external_id = external_id
        if external_id_type is not None:
            self.external_id_type = external_id_type

    @property
    def comment(self):
        """Gets the comment of this NewActivity.  # noqa: E501


        :return: The comment of this NewActivity.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this NewActivity.


        :param comment: The comment of this NewActivity.  # noqa: E501
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

    @property
    def start_date(self):
        """Gets the start_date of this NewActivity.  # noqa: E501


        :return: The start_date of this NewActivity.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this NewActivity.


        :param start_date: The start_date of this NewActivity.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this NewActivity.  # noqa: E501


        :return: The end_date of this NewActivity.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this NewActivity.


        :param end_date: The end_date of this NewActivity.  # noqa: E501
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def event_type(self):
        """Gets the event_type of this NewActivity.  # noqa: E501


        :return: The event_type of this NewActivity.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this NewActivity.


        :param event_type: The event_type of this NewActivity.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def is_public(self):
        """Gets the is_public of this NewActivity.  # noqa: E501


        :return: The is_public of this NewActivity.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this NewActivity.


        :param is_public: The is_public of this NewActivity.  # noqa: E501
        :type: bool
        """
        if is_public is None:
            raise ValueError("Invalid value for `is_public`, must not be `None`")  # noqa: E501

        self._is_public = is_public

    @property
    def title(self):
        """Gets the title of this NewActivity.  # noqa: E501


        :return: The title of this NewActivity.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NewActivity.


        :param title: The title of this NewActivity.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def repeatable(self):
        """Gets the repeatable of this NewActivity.  # noqa: E501


        :return: The repeatable of this NewActivity.  # noqa: E501
        :rtype: bool
        """
        return self._repeatable

    @repeatable.setter
    def repeatable(self, repeatable):
        """Sets the repeatable of this NewActivity.


        :param repeatable: The repeatable of this NewActivity.  # noqa: E501
        :type: bool
        """
        if repeatable is None:
            raise ValueError("Invalid value for `repeatable`, must not be `None`")  # noqa: E501

        self._repeatable = repeatable

    @property
    def repeat_interval(self):
        """Gets the repeat_interval of this NewActivity.  # noqa: E501


        :return: The repeat_interval of this NewActivity.  # noqa: E501
        :rtype: int
        """
        return self._repeat_interval

    @repeat_interval.setter
    def repeat_interval(self, repeat_interval):
        """Sets the repeat_interval of this NewActivity.


        :param repeat_interval: The repeat_interval of this NewActivity.  # noqa: E501
        :type: int
        """

        self._repeat_interval = repeat_interval

    @property
    def repeat_type(self):
        """Gets the repeat_type of this NewActivity.  # noqa: E501


        :return: The repeat_type of this NewActivity.  # noqa: E501
        :rtype: int
        """
        return self._repeat_type

    @repeat_type.setter
    def repeat_type(self, repeat_type):
        """Sets the repeat_type of this NewActivity.


        :param repeat_type: The repeat_type of this NewActivity.  # noqa: E501
        :type: int
        """

        self._repeat_type = repeat_type

    @property
    def repetitions(self):
        """Gets the repetitions of this NewActivity.  # noqa: E501


        :return: The repetitions of this NewActivity.  # noqa: E501
        :rtype: int
        """
        return self._repetitions

    @repetitions.setter
    def repetitions(self, repetitions):
        """Sets the repetitions of this NewActivity.


        :param repetitions: The repetitions of this NewActivity.  # noqa: E501
        :type: int
        """

        self._repetitions = repetitions

    @property
    def external_id(self):
        """Gets the external_id of this NewActivity.  # noqa: E501


        :return: The external_id of this NewActivity.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this NewActivity.


        :param external_id: The external_id of this NewActivity.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def external_id_type(self):
        """Gets the external_id_type of this NewActivity.  # noqa: E501


        :return: The external_id_type of this NewActivity.  # noqa: E501
        :rtype: int
        """
        return self._external_id_type

    @external_id_type.setter
    def external_id_type(self, external_id_type):
        """Sets the external_id_type of this NewActivity.


        :param external_id_type: The external_id_type of this NewActivity.  # noqa: E501
        :type: int
        """

        self._external_id_type = external_id_type

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
        if not isinstance(other, NewActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
