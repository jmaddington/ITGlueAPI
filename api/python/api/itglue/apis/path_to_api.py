import typing_extensions

from itglue.paths import PathValues
from itglue.apis.paths.organizations import Organizations
from itglue.apis.paths.organizations_id import OrganizationsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.ORGANIZATIONS_ID: OrganizationsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.ORGANIZATIONS_ID: OrganizationsId,
    }
)
