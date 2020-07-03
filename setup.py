# coding: utf-8

"""
    Cloud Speech-to-Text API

    Converts audio to text by applying powerful neural network models. <br> **PLEASE NOTE**: This API is provided by Google, beside the documentation provide below, you can find Google API documentation [here](https://cloud.google.com/speech-to-text/docs/reference/rest). You can refer to the Google documentation as well except by the URLs needed to call the API and that are documented here below.  # noqa: E501

    OpenAPI spec version: v3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "gcloud-speech-to-text"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Cloud Speech-to-Text API",
    author_email="",
    url="",
    keywords=["Swagger", "Cloud Speech-to-Text API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Converts audio to text by applying powerful neural network models. &lt;br&gt; **PLEASE NOTE**: This API is provided by Google, beside the documentation provide below, you can find Google API documentation [here](https://cloud.google.com/speech-to-text/docs/reference/rest). You can refer to the Google documentation as well except by the URLs needed to call the API and that are documented here below.  # noqa: E501
    """
)