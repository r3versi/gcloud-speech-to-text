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


class SpeechRecognitionAlternative(object):
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
        'confidence': 'float',
        'transcript': 'str',
        'words': 'list[WordInfo]'
    }

    attribute_map = {
        'confidence': 'confidence',
        'transcript': 'transcript',
        'words': 'words'
    }

    def __init__(self, confidence=None, transcript=None, words=None):  # noqa: E501
        """SpeechRecognitionAlternative - a model defined in Swagger"""  # noqa: E501
        self._confidence = None
        self._transcript = None
        self._words = None
        self.discriminator = None
        if confidence is not None:
            self.confidence = confidence
        if transcript is not None:
            self.transcript = transcript
        if words is not None:
            self.words = words

    @property
    def confidence(self):
        """Gets the confidence of this SpeechRecognitionAlternative.  # noqa: E501

        The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. This field is set only for the top alternative of a non-streaming result or, of a streaming result where `is_final=true`. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating `confidence` was not set.  # noqa: E501

        :return: The confidence of this SpeechRecognitionAlternative.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this SpeechRecognitionAlternative.

        The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. This field is set only for the top alternative of a non-streaming result or, of a streaming result where `is_final=true`. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating `confidence` was not set.  # noqa: E501

        :param confidence: The confidence of this SpeechRecognitionAlternative.  # noqa: E501
        :type: float
        """

        self._confidence = confidence

    @property
    def transcript(self):
        """Gets the transcript of this SpeechRecognitionAlternative.  # noqa: E501

        Transcript text representing the words that the user spoke.  # noqa: E501

        :return: The transcript of this SpeechRecognitionAlternative.  # noqa: E501
        :rtype: str
        """
        return self._transcript

    @transcript.setter
    def transcript(self, transcript):
        """Sets the transcript of this SpeechRecognitionAlternative.

        Transcript text representing the words that the user spoke.  # noqa: E501

        :param transcript: The transcript of this SpeechRecognitionAlternative.  # noqa: E501
        :type: str
        """

        self._transcript = transcript

    @property
    def words(self):
        """Gets the words of this SpeechRecognitionAlternative.  # noqa: E501

        A list of word-specific information for each recognized word. Note: When `enable_speaker_diarization` is true, you will see all the words from the beginning of the audio.  # noqa: E501

        :return: The words of this SpeechRecognitionAlternative.  # noqa: E501
        :rtype: list[WordInfo]
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this SpeechRecognitionAlternative.

        A list of word-specific information for each recognized word. Note: When `enable_speaker_diarization` is true, you will see all the words from the beginning of the audio.  # noqa: E501

        :param words: The words of this SpeechRecognitionAlternative.  # noqa: E501
        :type: list[WordInfo]
        """

        self._words = words

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
        if issubclass(SpeechRecognitionAlternative, dict):
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
        if not isinstance(other, SpeechRecognitionAlternative):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
