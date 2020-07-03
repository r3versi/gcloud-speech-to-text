# coding: utf-8

"""
    Cloud Speech-to-Text API

    Converts audio to text by applying powerful neural network models. <br> **PLEASE NOTE**: This API is provided by Google, beside the documentation provide below, you can find Google API documentation [here](https://cloud.google.com/speech-to-text/docs/reference/rest). You can refer to the Google documentation as well except by the URLs needed to call the API and that are documented here below.  # noqa: E501

    OpenAPI spec version: v3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class RecognizeResponse(object):
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
        'results': 'list[SpeechRecognitionResult]'
    }

    attribute_map = {
        'results': 'results'
    }

    def __init__(self, results=None):  # noqa: E501
        """RecognizeResponse - a model defined in Swagger"""  # noqa: E501
        self._results = None
        self.discriminator = None
        if results is not None:
            self.results = results

    @property
    def results(self):
        """Gets the results of this RecognizeResponse.  # noqa: E501

        Sequential list of transcription results corresponding to sequential portions of audio.  # noqa: E501

        :return: The results of this RecognizeResponse.  # noqa: E501
        :rtype: list[SpeechRecognitionResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this RecognizeResponse.

        Sequential list of transcription results corresponding to sequential portions of audio.  # noqa: E501

        :param results: The results of this RecognizeResponse.  # noqa: E501
        :type: list[SpeechRecognitionResult]
        """

        self._results = results

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
        if issubclass(RecognizeResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecognizeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
