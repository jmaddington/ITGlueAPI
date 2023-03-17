import typing_extensions

from itglue.apis.tags import TagValues
from itglue.apis.tags.organizations_api import OrganizationsApi
from itglue.apis.tags.organization_types_api import OrganizationTypesApi
from itglue.apis.tags.organization_statuses_api import OrganizationStatusesApi
from itglue.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.ORGANIZATION_TYPES: OrganizationTypesApi,
        TagValues.ORGANIZATION_STATUSES: OrganizationStatusesApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.ORGANIZATION_TYPES: OrganizationTypesApi,
        TagValues.ORGANIZATION_STATUSES: OrganizationStatusesApi,
        TagValues.DEFAULT: DefaultApi,
    }
)
