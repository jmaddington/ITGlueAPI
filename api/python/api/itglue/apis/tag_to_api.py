import typing_extensions

from itglue.apis.tags import TagValues
from itglue.apis.tags.organization_types_api import OrganizationTypesApi
from itglue.apis.tags.organization_statuses_api import OrganizationStatusesApi
from itglue.apis.tags.organizations_api import OrganizationsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ORGANIZATION_TYPES: OrganizationTypesApi,
        TagValues.ORGANIZATION_STATUSES: OrganizationStatusesApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ORGANIZATION_TYPES: OrganizationTypesApi,
        TagValues.ORGANIZATION_STATUSES: OrganizationStatusesApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
    }
)
