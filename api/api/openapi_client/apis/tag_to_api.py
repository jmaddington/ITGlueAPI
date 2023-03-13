import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.organizations_api import OrganizationsApi
from openapi_client.apis.tags.organization_types_api import OrganizationTypesApi
from openapi_client.apis.tags.organization_statuses_api import OrganizationStatusesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.ORGANIZATION_TYPES: OrganizationTypesApi,
        TagValues.ORGANIZATION_STATUSES: OrganizationStatusesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.ORGANIZATION_TYPES: OrganizationTypesApi,
        TagValues.ORGANIZATION_STATUSES: OrganizationStatusesApi,
    }
)
