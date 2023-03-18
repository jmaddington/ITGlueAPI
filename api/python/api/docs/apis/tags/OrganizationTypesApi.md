<a name="__pageTop"></a>
# itglue.apis.tags.organization_types_api.OrganizationTypesApi

All URIs are relative to *https://api.itglue.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_status**](#create_organization_status) | **post** /organization_statuses | Create an organization status
[**create_organization_type**](#create_organization_type) | **post** /organization_types | Create an organization type.
[**index_organization_statuses**](#index_organization_statuses) | **get** /organization_statuses | List all OrganizationStatuses
[**index_organization_types**](#index_organization_types) | **get** /organization_types | List all organization types.
[**show_organization_type**](#show_organization_type) | **get** /organization_types/{id} | Show an organization type.
[**update_organization_type**](#update_organization_type) | **patch** /organization_types/{id} | Update an organization type.

# **create_organization_status**
<a name="create_organization_status"></a>
> OrganizationStatus create_organization_status(organization_status)

Create an organization status

Creates a new organization status in your account. Returns the created object if successful.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import organization_types_api
from itglue.model.organization_status import OrganizationStatus
from pprint import pprint
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
    api_instance = organization_types_api.OrganizationTypesApi(api_client)

    # example passing only required values which don't have defaults set
    body = OrganizationStatus(
        id="id_example",
        type="type_example",
        attributes=dict(
            name="name_example",
            created_at="1970-01-01T00:00:00.00Z",
            updated_at="1970-01-01T00:00:00.00Z",
        ),
    )
    try:
        # Create an organization status
        api_response = api_instance.create_organization_status(
            body=body,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationTypesApi->create_organization_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndApijsoncharsetutf8] | required |
content_type | str | optional, default is 'application/vnd.api+json;charset&#x3D;utf-8' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndApijsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationStatus**](../../models/OrganizationStatus.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_organization_status.ApiResponseFor200) | Successfully created the organization status
401 | [ApiResponseFor401](#create_organization_status.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_organization_status.ApiResponseFor403) | Forbidden
415 | [ApiResponseFor415](#create_organization_status.ApiResponseFor415) | Bad Content Type
422 | [ApiResponseFor422](#create_organization_status.ApiResponseFor422) | Bad Request

#### create_organization_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationStatus**](../../models/OrganizationStatus.md) |  | 


#### create_organization_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_organization_status.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_organization_status.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_organization_status.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_organization_type**
<a name="create_organization_type"></a>
> OrganizationType create_organization_type(organization_type)

Create an organization type.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import organization_types_api
from itglue.model.organization_type import OrganizationType
from pprint import pprint
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
    api_instance = organization_types_api.OrganizationTypesApi(api_client)

    # example passing only required values which don't have defaults set
    body = OrganizationType(
        id="id_example",
        type="type_example",
        attributes=dict(
            name="name_example",
            created_at="1970-01-01T00:00:00.00Z",
            updated_at="1970-01-01T00:00:00.00Z",
        ),
    )
    try:
        # Create an organization type.
        api_response = api_instance.create_organization_type(
            body=body,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationTypesApi->create_organization_type: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndApijsonCharsetutf8] | required |
content_type | str | optional, default is 'application/vnd.api+json; charset&#x3D;utf-8' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json; charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndApijsonCharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationType**](../../models/OrganizationType.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_organization_type.ApiResponseFor200) | Returns the created object if successful.
401 | [ApiResponseFor401](#create_organization_type.ApiResponseFor401) | Unauthorized
422 | [ApiResponseFor422](#create_organization_type.ApiResponseFor422) | Bad Request
415 | [ApiResponseFor415](#create_organization_type.ApiResponseFor415) | Bad Content Type
403 | [ApiResponseFor403](#create_organization_type.ApiResponseFor403) | Forbidden

#### create_organization_type.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationType**](../../models/OrganizationType.md) |  | 


#### create_organization_type.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_organization_type.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_organization_type.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_organization_type.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **index_organization_statuses**
<a name="index_organization_statuses"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} index_organization_statuses()

List all OrganizationStatuses

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import organization_types_api
from itglue.model.organization_status import OrganizationStatus
from pprint import pprint
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
    api_instance = organization_types_api.OrganizationTypesApi(api_client)

    # example passing only optional values
    query_params = {
        'filter': OrganizationStatus(
        id="id_example",
        type="type_example",
        attributes=dict(
            name="name_example",
            created_at="1970-01-01T00:00:00.00Z",
            updated_at="1970-01-01T00:00:00.00Z",
        ),
    ),
        'sort': "name",
        'page': dict(
        number=1,
        size=1,
    ),
    }
    try:
        # List all OrganizationStatuses
        api_response = api_instance.index_organization_statuses(
            query_params=query_params,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationTypesApi->index_organization_statuses: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filter | FilterSchema | | optional
sort | SortSchema | | optional
page | PageSchema | | optional


# FilterSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationStatus**](../../models/OrganizationStatus.md) |  | 


# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["name", "id", "created_at", "updated_at", ] 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**number** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#index_organization_statuses.ApiResponseFor200) | A list of organization statuses in your account.
401 | [ApiResponseFor401](#index_organization_statuses.ApiResponseFor401) | Unauthorized

#### index_organization_statuses.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrganizationStatus**]({{complexTypePrefix}}OrganizationStatus.md) | [**OrganizationStatus**]({{complexTypePrefix}}OrganizationStatus.md) | [**OrganizationStatus**]({{complexTypePrefix}}OrganizationStatus.md) |  | 

#### index_organization_statuses.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **index_organization_types**
<a name="index_organization_types"></a>
> Organization index_organization_types()

List all organization types.

List all organization types in your account.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import organization_types_api
from itglue.model.organization import Organization
from pprint import pprint
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
    api_instance = organization_types_api.OrganizationTypesApi(api_client)

    # example passing only optional values
    query_params = {
        'filter': dict(
        name="name_example",
    ),
        'sort': "name",
        'page': dict(
        number=3.14,
        size=3.14,
    ),
    }
    try:
        # List all organization types.
        api_response = api_instance.index_organization_types(
            query_params=query_params,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationTypesApi->index_organization_types: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json; charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filter | FilterSchema | | optional
sort | SortSchema | | optional
page | PageSchema | | optional


# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Param Type: CGI Notes: Comma separated values  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["name", "id", "updated_at", "created_at", ] 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**number** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**size** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#index_organization_types.ApiResponseFor200) | A successful response
401 | [ApiResponseFor401](#index_organization_types.ApiResponseFor401) | Unauthorized

#### index_organization_types.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**Organization**](../../models/Organization.md) |  | 


#### index_organization_types.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **show_organization_type**
<a name="show_organization_type"></a>
> OrganizationType show_organization_type(id)

Show an organization type.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import organization_types_api
from itglue.model.organization_type import OrganizationType
from pprint import pprint
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
    api_instance = organization_types_api.OrganizationTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 86,
    }
    try:
        # Show an organization type.
        api_response = api_instance.show_organization_type(
            path_params=path_params,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationTypesApi->show_organization_type: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#show_organization_type.ApiResponseFor200) | Details of an existing organization type.
401 | [ApiResponseFor401](#show_organization_type.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#show_organization_type.ApiResponseFor404) | Not Found

#### show_organization_type.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationType**](../../models/OrganizationType.md) |  | 


#### show_organization_type.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### show_organization_type.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_organization_type**
<a name="update_organization_type"></a>
> OrganizationType update_organization_type(idorganization_type)

Update an organization type.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import organization_types_api
from itglue.model.organization_type import OrganizationType
from pprint import pprint
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
    api_instance = organization_types_api.OrganizationTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 86,
    }
    body = OrganizationType(
        id="id_example",
        type="type_example",
        attributes=dict(
            name="name_example",
            created_at="1970-01-01T00:00:00.00Z",
            updated_at="1970-01-01T00:00:00.00Z",
        ),
    )
    try:
        # Update an organization type.
        api_response = api_instance.update_organization_type(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationTypesApi->update_organization_type: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndApijsonCharsetutf8] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.api+json charset&#x3D;utf-8' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndApijsonCharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationType**](../../models/OrganizationType.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_organization_type.ApiResponseFor200) | Successfully updated organization type.
401 | [ApiResponseFor401](#update_organization_type.ApiResponseFor401) | Unauthorized
422 | [ApiResponseFor422](#update_organization_type.ApiResponseFor422) | Bad Request
415 | [ApiResponseFor415](#update_organization_type.ApiResponseFor415) | Bad Content Type
404 | [ApiResponseFor404](#update_organization_type.ApiResponseFor404) | Not Found

#### update_organization_type.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationType**](../../models/OrganizationType.md) |  | 


#### update_organization_type.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_organization_type.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_organization_type.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_organization_type.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

