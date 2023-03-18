import typing_extensions

from itglue.paths import PathValues
from itglue.apis.paths.organization_types import OrganizationTypes
from itglue.apis.paths.organization_types_id import OrganizationTypesId
from itglue.apis.paths.organization_statuses import OrganizationStatuses
from itglue.apis.paths.organization_statuses_id import OrganizationStatusesId
from itglue.apis.paths.organizations import Organizations
from itglue.apis.paths.organizations_id import OrganizationsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ORGANIZATION_TYPES: OrganizationTypes,
        PathValues.ORGANIZATION_TYPES_ID: OrganizationTypesId,
        PathValues.ORGANIZATION_STATUSES: OrganizationStatuses,
        PathValues.ORGANIZATION_STATUSES_ID: OrganizationStatusesId,
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.ORGANIZATIONS_ID: OrganizationsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ORGANIZATION_TYPES: OrganizationTypes,
        PathValues.ORGANIZATION_TYPES_ID: OrganizationTypesId,
        PathValues.ORGANIZATION_STATUSES: OrganizationStatuses,
        PathValues.ORGANIZATION_STATUSES_ID: OrganizationStatusesId,
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.ORGANIZATIONS_ID: OrganizationsId,
    }
)
