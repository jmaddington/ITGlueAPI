# coding: utf-8

"""
    IT Glue API in OpenAPI Spec

    This is the IT Glue API implemented in OpenAPI 3.0 specification.  You can find out more about Swagger at [https://swagger.io](https://swagger.io).  Some useful links: - [Reference](https://api.itglue.com/developer/)  # noqa: E501

    The version of the OpenAPI document: 0.0.01
    Contact: jonathan.addington@jmaddington.com
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "openapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi >= 14.5.14",
    "frozendict ~= 2.3.4",
    "python-dateutil ~= 2.7.0",
    "setuptools >= 21.0.0",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.7",
]

setup(
    name=NAME,
    version=VERSION,
    description="IT Glue API in OpenAPI Spec",
    author="OpenAPI Generator community",
    author_email="jonathan.addington@jmaddington.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "IT Glue API in OpenAPI Spec"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="None",
    long_description="""\
    This is the IT Glue API implemented in OpenAPI 3.0 specification.  You can find out more about Swagger at [https://swagger.io](https://swagger.io).  Some useful links: - [Reference](https://api.itglue.com/developer/)  # noqa: E501
    """
)
