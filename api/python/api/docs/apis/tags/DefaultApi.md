<a name="__pageTop"></a>
# itglue.apis.tags.default_api.DefaultApi

All URIs are relative to *https://api.itglue.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_id_patch**](#organizations_id_patch) | **patch** /organizations/{id} | Update an organization

# **organizations_id_patch**
<a name="organizations_id_patch"></a>
> Organization organizations_id_patch(iddata)

Update an organization

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 3.14,
    }
    query_params = {
        'data': dict(
        type="organizations",
        attributes=dict(
            id=1,
            name="name_example",
            alert="alert_example",
            description="description_example",
            organization_type_id=1,
            organization_status_id=1,
            quick_notes="quick_notes_example",
            short_name="short_name_example",
        ),
    ),
    }
    try:
        # Update an organization
        api_response = api_instance.organizations_id_patch(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling DefaultApi->organizations_id_patch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 3.14,
    }
    query_params = {
        'data': dict(
        type="organizations",
        attributes=dict(
            id=1,
            name="name_example",
            alert="alert_example",
            description="description_example",
            organization_type_id=1,
            organization_status_id=1,
            quick_notes="quick_notes_example",
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
        # Update an organization
        api_response = api_instance.organizations_id_patch(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling DefaultApi->organizations_id_patch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndApijson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
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
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**name** | None, str,  | NoneClass, str,  |  | [optional] 
**alert** | None, str,  | NoneClass, str,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  |  | [optional] 
**organization_type_id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**organization_status_id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**quick_notes** | None, str,  | NoneClass, str,  |  | [optional] 
**short_name** | None, str,  | NoneClass, str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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
200 | [ApiResponseFor200](#organizations_id_patch.ApiResponseFor200) | A successful response
401 | [ApiResponseFor401](#organizations_id_patch.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#organizations_id_patch.ApiResponseFor404) | Not Found
415 | [ApiResponseFor415](#organizations_id_patch.ApiResponseFor415) | Bad Content Type
422 | [ApiResponseFor422](#organizations_id_patch.ApiResponseFor422) | Bad Request

#### organizations_id_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsonCharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**Organization**](../../models/Organization.md) |  | 


#### organizations_id_patch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### organizations_id_patch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### organizations_id_patch.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### organizations_id_patch.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

