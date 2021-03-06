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


class SpeakerDiarizationConfig(object):
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
        'enable_speaker_diarization': 'bool',
        'min_speaker_count': 'int',
        'max_speaker_count': 'int',
        'speaker_tag': 'int'
    }

    attribute_map = {
        'enable_speaker_diarization': 'enableSpeakerDiarization',
        'min_speaker_count': 'minSpeakerCount',
        'max_speaker_count': 'maxSpeakerCount',
        'speaker_tag': 'speakerTag'
    }

    def __init__(self, enable_speaker_diarization=None, min_speaker_count=None, max_speaker_count=None, speaker_tag=None):  # noqa: E501
        """SpeakerDiarizationConfig - a model defined in Swagger"""  # noqa: E501
        self._enable_speaker_diarization = None
        self._min_speaker_count = None
        self._max_speaker_count = None
        self._speaker_tag = None
        self.discriminator = None
        if enable_speaker_diarization is not None:
            self.enable_speaker_diarization = enable_speaker_diarization
        if min_speaker_count is not None:
            self.min_speaker_count = min_speaker_count
        if max_speaker_count is not None:
            self.max_speaker_count = max_speaker_count
        if speaker_tag is not None:
            self.speaker_tag = speaker_tag

    @property
    def enable_speaker_diarization(self):
        """Gets the enable_speaker_diarization of this SpeakerDiarizationConfig.  # noqa: E501

        If 'true', enables speaker detection for each recognized word in the top alternative of the recognition result using a speaker_tag provided in the WordInfo.  # noqa: E501

        :return: The enable_speaker_diarization of this SpeakerDiarizationConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enable_speaker_diarization

    @enable_speaker_diarization.setter
    def enable_speaker_diarization(self, enable_speaker_diarization):
        """Sets the enable_speaker_diarization of this SpeakerDiarizationConfig.

        If 'true', enables speaker detection for each recognized word in the top alternative of the recognition result using a speaker_tag provided in the WordInfo.  # noqa: E501

        :param enable_speaker_diarization: The enable_speaker_diarization of this SpeakerDiarizationConfig.  # noqa: E501
        :type: bool
        """

        self._enable_speaker_diarization = enable_speaker_diarization

    @property
    def min_speaker_count(self):
        """Gets the min_speaker_count of this SpeakerDiarizationConfig.  # noqa: E501

        Minimum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 2.  # noqa: E501

        :return: The min_speaker_count of this SpeakerDiarizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._min_speaker_count

    @min_speaker_count.setter
    def min_speaker_count(self, min_speaker_count):
        """Sets the min_speaker_count of this SpeakerDiarizationConfig.

        Minimum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 2.  # noqa: E501

        :param min_speaker_count: The min_speaker_count of this SpeakerDiarizationConfig.  # noqa: E501
        :type: int
        """

        self._min_speaker_count = min_speaker_count

    @property
    def max_speaker_count(self):
        """Gets the max_speaker_count of this SpeakerDiarizationConfig.  # noqa: E501

        Maximum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 6.  # noqa: E501

        :return: The max_speaker_count of this SpeakerDiarizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_speaker_count

    @max_speaker_count.setter
    def max_speaker_count(self, max_speaker_count):
        """Sets the max_speaker_count of this SpeakerDiarizationConfig.

        Maximum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 6.  # noqa: E501

        :param max_speaker_count: The max_speaker_count of this SpeakerDiarizationConfig.  # noqa: E501
        :type: int
        """

        self._max_speaker_count = max_speaker_count

    @property
    def speaker_tag(self):
        """Gets the speaker_tag of this SpeakerDiarizationConfig.  # noqa: E501

        Output only. Unused.  # noqa: E501

        :return: The speaker_tag of this SpeakerDiarizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._speaker_tag

    @speaker_tag.setter
    def speaker_tag(self, speaker_tag):
        """Sets the speaker_tag of this SpeakerDiarizationConfig.

        Output only. Unused.  # noqa: E501

        :param speaker_tag: The speaker_tag of this SpeakerDiarizationConfig.  # noqa: E501
        :type: int
        """

        self._speaker_tag = speaker_tag

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
        if issubclass(SpeakerDiarizationConfig, dict):
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
        if not isinstance(other, SpeakerDiarizationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
