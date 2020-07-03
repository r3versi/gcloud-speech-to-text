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


class RecognizeRequest(object):
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
        'config': 'RecognitionConfig',
        'audio': 'RecognitionAudio'
    }

    attribute_map = {
        'config': 'config',
        'audio': 'audio'
    }

    def __init__(self, config=None, audio=None):  # noqa: E501
        """RecognizeRequest - a model defined in Swagger"""  # noqa: E501
        self._config = None
        self._audio = None
        self.discriminator = None
        if config is not None:
            self.config = config
        if audio is not None:
            self.audio = audio

    @property
    def config(self):
        """Gets the config of this RecognizeRequest.  # noqa: E501


        :return: The config of this RecognizeRequest.  # noqa: E501
        :rtype: RecognitionConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this RecognizeRequest.


        :param config: The config of this RecognizeRequest.  # noqa: E501
        :type: RecognitionConfig
        """

        self._config = config

    @property
    def audio(self):
        """Gets the audio of this RecognizeRequest.  # noqa: E501


        :return: The audio of this RecognizeRequest.  # noqa: E501
        :rtype: RecognitionAudio
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this RecognizeRequest.


        :param audio: The audio of this RecognizeRequest.  # noqa: E501
        :type: RecognitionAudio
        """

        self._audio = audio

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
        if issubclass(RecognizeRequest, dict):
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
        if not isinstance(other, RecognizeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
