<a name="__pageTop"></a>
# itglue.apis.tags.organization_statuses_api.OrganizationStatusesApi

All URIs are relative to *https://api.itglue.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_organization_status**](#show_organization_status) | **get** /organization_statuses/{id} | Show an organization status
[**update_organization_status**](#update_organization_status) | **patch** /organization_statuses/{id} | Update an organization status

# **show_organization_status**
<a name="show_organization_status"></a>
> OrganizationStatus show_organization_status(id)

Show an organization status

Returns the details of an existing organization status

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import organization_statuses_api
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
    api_instance = organization_statuses_api.OrganizationStatusesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Show an organization status
        api_response = api_instance.show_organization_status(
            path_params=path_params,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationStatusesApi->show_organization_status: %s\n" % e)
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
200 | [ApiResponseFor200](#show_organization_status.ApiResponseFor200) | Successfully retrieved the organization status
401 | [ApiResponseFor401](#show_organization_status.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#show_organization_status.ApiResponseFor404) | Not Found

#### show_organization_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationStatus**](../../models/OrganizationStatus.md) |  | 


#### show_organization_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### show_organization_status.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_organization_status**
<a name="update_organization_status"></a>
> OrganizationStatus update_organization_status(idorganization_status)

Update an organization status

Updates an organization status in your account.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import itglue
from itglue.apis.tags import organization_statuses_api
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
    api_instance = organization_statuses_api.OrganizationStatusesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
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
        # Update an organization status
        api_response = api_instance.update_organization_status(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except itglue.ApiException as e:
        print("Exception when calling OrganizationStatusesApi->update_organization_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndApijsoncharsetutf8] | required |
path_params | RequestPathParams | |
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
200 | [ApiResponseFor200](#update_organization_status.ApiResponseFor200) | Successfully created the organization status
401 | [ApiResponseFor401](#update_organization_status.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#update_organization_status.ApiResponseFor403) | Forbidden
415 | [ApiResponseFor415](#update_organization_status.ApiResponseFor415) | Bad Content Type
422 | [ApiResponseFor422](#update_organization_status.ApiResponseFor422) | Bad Request

#### update_organization_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijsoncharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationStatus**](../../models/OrganizationStatus.md) |  | 


#### update_organization_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_organization_status.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_organization_status.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_organization_status.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

