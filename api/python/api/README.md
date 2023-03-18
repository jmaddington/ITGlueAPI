# itglue
This is the IT Glue API implemented in OpenAPI 3.0 specification.  You can find out more about
Swagger at [https://swagger.io](https://swagger.io).

Some useful links:
- [Reference](https://api.itglue.com/developer/)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.01
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import itglue
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import itglue
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import itglue
from pprint import pprint
from itglue.apis.tags import organizations_api
from itglue.model.organization import Organization
# Defining the host is optional and defaults to https://api.itglue.com
# See configuration.py for a list of all supported configuration parameters.
configuration = itglue.Configuration(
    host = "https://api.itglue.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with itglue.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    data = dict(
        type="organizations",
        attributes=dict(
            name="name_example",
            description="description_example",
            organization_type_id=1,
            organization_status_id=1,
            quick_notes="quick_notes_example",
            alert="alert_example",
            short_name="short_name_example",
        ),
    ) # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
organization = Organization(
        id=2,
        attributes=dict(
            name="Happy Frog",
            alert="THIS IS UNDEFINED",
            description="Happy frog is a demo",
            organization_type_id=86,
            organization_type_name="Customer",
            organization_status_id=68,
            organization_status_name="Active",
            primary=False,
            logo="NO EXAMPLES",
            quick_notes="quick_notes_example",
            short_name="Happy",
            created_at="1970-01-01T00:00:00.00Z",
            updated_at="1970-01-01T00:00:00.00Z",
        ),
    ) # Organization | Organization data to create a new organization. (optional)

    try:
        # Create an organization.
        api_response = api_instance.create_organization(dataorganization=organization)
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.itglue.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OrganizationsApi* | [**create_organization**](docs/apis/tags/OrganizationsApi.md#create_organization) | **post** /organizations | Create an organization.
*OrganizationsApi* | [**index_organizations**](docs/apis/tags/OrganizationsApi.md#index_organizations) | **get** /organizations | Returns a list of organizations in your account.
*OrganizationsApi* | [**organizations_id_get**](docs/apis/tags/OrganizationsApi.md#organizations_id_get) | **get** /organizations/{id} | Retrieve an organization
*DefaultApi* | [**organizations_id_patch**](docs/apis/tags/DefaultApi.md#organizations_id_patch) | **patch** /organizations/{id} | Update an organization

## Documentation For Models

 - [Organization](docs/models/Organization.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author

jonathan.addington@jmaddington.com
jonathan.addington@jmaddington.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in itglue.apis and itglue.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from itglue.apis.default_api import DefaultApi`
- `from itglue.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import itglue
from itglue.apis import *
from itglue.models import *
```