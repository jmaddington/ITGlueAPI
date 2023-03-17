<a name="__pageTop"></a>
# itglue.apis.tags.organizations_api.OrganizationsApi

All URIs are relative to *https://api.itglue.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization**](#create_organization) | **post** /organizations | Create an organization.
[**index_organizations**](#index_organizations) | **get** /organizations | Returns a list of organizations in your account.
[**organizations_id_get**](#organizations_id_get) | **get** /organizations/{id} | Retrieve an organization

# **create_organization**
<a name="create_organization"></a>
> Organization create_organization(data)

Create an organization.

Creates an organization. Returns the created object if successful.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import organizations_api
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'data': dict(
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
    ),
    }
    try:
        # Create an organization.
        api_response = api_instance.create_organization(
            query_params=query_params,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)

    # example passing only optional values
    query_params = {
        'data': dict(
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
    ),
    }
    body = Organization(
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
    )
    try:
        # Create an organization.
        api_response = api_instance.create_organization(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndApijson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/vnd.api+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json; charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**Organization**](../../models/Organization.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
data | DataSchema | | 


# DataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | [optional] must be one of ["organizations", ] 
**[attributes](#attributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  |  | [optional] 
**organization_type_id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**organization_status_id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**quick_notes** | None, str,  | NoneClass, str,  |  | [optional] 
**alert** | None, str,  | NoneClass, str,  |  | [optional] 
**short_name** | None, str,  | NoneClass, str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_organization.ApiResponseFor200) | A successful response
401 | [ApiResponseFor401](#create_organization.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_organization.ApiResponseFor403) | Forbidden
415 | [ApiResponseFor415](#create_organization.ApiResponseFor415) | Bad Content Type
422 | [ApiResponseFor422](#create_organization.ApiResponseFor422) | Bad Request

#### create_organization.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**Organization**](../../models/Organization.md) |  | 


#### create_organization.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_organization.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_organization.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_organization.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **index_organizations**
<a name="index_organizations"></a>
> Organization index_organizations()

Returns a list of organizations in your account.

Returns a list of organizations in your account.  Any quick notes on an organization will be truncated to the first 250 characters. The full quick notes are available via the Show request. 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import organizations_api
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only optional values
    query_params = {
        'filter': dict(
        id=3.14,
        name="name_example",
        organization_type_id=3.14,
        organization_status_id=3.14,
        created_at="created_at_example",
        updated_at="updated_at_example",
        my_glue_account_id=3.14,
        psa_id="psa_id_example",
        psa_integration_type="manage",
        group_id=3.14,
    ),
        'filter[exclude]': dict(
        id=3.14,
        name="name_example",
        organization_type_id=3.14,
        organization_status_id=3.14,
    ),
        'filter[range]': dict(
        my_glue_account_id=3.14,
    ),
        'sort': "name",
        'page': dict(
        number=3.14,
        size=3.14,
    ),
        'include': "adapters_resources",
    }
    body = Organization(
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
    )
    try:
        # Returns a list of organizations in your account.
        api_response = api_instance.index_organizations(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationsApi->index_organizations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndApijson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/vnd.api+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json; charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**Organization**](../../models/Organization.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filter | FilterSchema | | optional
filter[exclude] | FilterExcludeSchema | | optional
filter[range] | FilterRangeSchema | | optional
sort | SortSchema | | optional
page | PageSchema | | optional
include | IncludeSchema | | optional


# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**organization_type_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**organization_status_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**created_at** | str,  | str,  |  | [optional] 
**updated_at** | str,  | str,  |  | [optional] 
**my_glue_account_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**psa_id** | str,  | str,  |  | [optional] 
**psa_integration_type** | str,  | str,  |  | [optional] must be one of ["manage", "autotask", "tigerpaw", "kaseya-bms", "pulseway-psa", "vorex", ] 
**group_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# FilterExcludeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**organization_type_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**organization_status_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# FilterRangeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**my_glue_account_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["name", "id", "updated_at", "organization_status_name", "organization_type_name", "created_at", "short_name", "my_glue_account_id", ] 

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

# IncludeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["adapters_resources", "attachments", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#index_organizations.ApiResponseFor200) | A successful response

#### index_organizations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**Organization**](../../models/Organization.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **organizations_id_get**
<a name="organizations_id_get"></a>
> Organization organizations_id_get(id)

Retrieve an organization

Returns the details of an existing organization.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import organizations_api
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 3.14,
    }
    query_params = {
    }
    try:
        # Retrieve an organization
        api_response = api_instance.organizations_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationsApi->organizations_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 3.14,
    }
    query_params = {
        'include': "adapters_resources",
    }
    try:
        # Retrieve an organization
        api_response = api_instance.organizations_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationsApi->organizations_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json; charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
include | IncludeSchema | | optional


# IncludeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["adapters_resources", "attachments", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#organizations_id_get.ApiResponseFor200) | A successful response
401 | [ApiResponseFor401](#organizations_id_get.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#organizations_id_get.ApiResponseFor404) | Not Found

#### organizations_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**Organization**](../../models/Organization.md) |  | 


#### organizations_id_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### organizations_id_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

