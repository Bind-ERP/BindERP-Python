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

from swagger_client.models.i_edm_term import IEdmTerm  # noqa: F401,E501
from swagger_client.models.i_edm_vocabulary_annotatable import IEdmVocabularyAnnotatable  # noqa: F401,E501


class IEdmVocabularyAnnotation(object):
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
        'qualifier': 'str',
        'term': 'IEdmTerm',
        'target': 'IEdmVocabularyAnnotatable'
    }

    attribute_map = {
        'qualifier': 'Qualifier',
        'term': 'Term',
        'target': 'Target'
    }

    def __init__(self, qualifier=None, term=None, target=None):  # noqa: E501
        """IEdmVocabularyAnnotation - a model defined in Swagger"""  # noqa: E501

        self._qualifier = None
        self._term = None
        self._target = None
        self.discriminator = None

        if qualifier is not None:
            self.qualifier = qualifier
        if term is not None:
            self.term = term
        if target is not None:
            self.target = target

    @property
    def qualifier(self):
        """Gets the qualifier of this IEdmVocabularyAnnotation.  # noqa: E501


        :return: The qualifier of this IEdmVocabularyAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._qualifier

    @qualifier.setter
    def qualifier(self, qualifier):
        """Sets the qualifier of this IEdmVocabularyAnnotation.


        :param qualifier: The qualifier of this IEdmVocabularyAnnotation.  # noqa: E501
        :type: str
        """

        self._qualifier = qualifier

    @property
    def term(self):
        """Gets the term of this IEdmVocabularyAnnotation.  # noqa: E501


        :return: The term of this IEdmVocabularyAnnotation.  # noqa: E501
        :rtype: IEdmTerm
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this IEdmVocabularyAnnotation.


        :param term: The term of this IEdmVocabularyAnnotation.  # noqa: E501
        :type: IEdmTerm
        """

        self._term = term

    @property
    def target(self):
        """Gets the target of this IEdmVocabularyAnnotation.  # noqa: E501


        :return: The target of this IEdmVocabularyAnnotation.  # noqa: E501
        :rtype: IEdmVocabularyAnnotatable
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this IEdmVocabularyAnnotation.


        :param target: The target of this IEdmVocabularyAnnotation.  # noqa: E501
        :type: IEdmVocabularyAnnotatable
        """

        self._target = target

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
        if not isinstance(other, IEdmVocabularyAnnotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
