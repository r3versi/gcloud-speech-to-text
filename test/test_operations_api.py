# coding: utf-8

"""
    Cloud Speech-to-Text API

    Converts audio to text by applying powerful neural network models. <br> **PLEASE NOTE**: This API is provided by Google, beside the documentation provide below, you can find Google API documentation [here](https://cloud.google.com/speech-to-text/docs/reference/rest). You can refer to the Google documentation as well except by the URLs needed to call the API and that are documented here below.  # noqa: E501

    OpenAPI spec version: v3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gcloudspeechtotext
from api.operations_api import OperationsApi  # noqa: E501
from gcloudspeechtotext.rest import ApiException


class TestOperationsApi(unittest.TestCase):
    """OperationsApi unit test stubs"""

    def setUp(self):
        self.api = api.operations_api.OperationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_speech_operations_get(self):
        """Test case for speech_operations_get

        """
        pass


if __name__ == '__main__':
    unittest.main()