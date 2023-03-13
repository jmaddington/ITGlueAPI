<a name="__pageTop"></a>
# openapi_client.apis.tags.organizations_api.OrganizationsApi

All URIs are relative to *https://api.itglue.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_organizations**](#index_organizations) | **get** /organizations | Returns a list of organizations in your account.

# **index_organizations**
<a name="index_organizations"></a>
> Organization index_organizations()

Returns a list of organizations in your account.

Returns a list of organizations in your account.  Any quick notes on an organization will be truncated to the first 250 characters. The full quick notes are available via the Show request. 

### Example

```python
import openapi_client
from openapi_client.apis.tags import organizations_api
from openapi_client.model.organization import Organization
from pprint import pprint
# Defining the host is optional and defaults to https://api.itglue.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.itglue.com"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only optional values
    query_params = {
        'filter': "filter_example",
        'filter[id]': 3.14,
        'filter[name]': "filter[name]_example",
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
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->index_organizations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndApijson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/vnd.api+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', ) | Tells the server the content type(s) that are accepted by the client
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
filter[id] | FilterIdSchema | | optional
filter[name] | FilterNameSchema | | optional


# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# FilterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#index_organizations.ApiResponseFor200) | Succeeded
401 | [ApiResponseFor401](#index_organizations.ApiResponseFor401) | Unauthorized
429 | [ApiResponseFor429](#index_organizations.ApiResponseFor429) | Too many requests

#### index_organizations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**Organization**](../../models/Organization.md) |  | 


#### index_organizations.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### index_organizations.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

