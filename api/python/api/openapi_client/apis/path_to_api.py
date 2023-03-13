import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.organizations import Organizations

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ORGANIZATIONS: Organizations,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ORGANIZATIONS: Organizations,
    }
)
