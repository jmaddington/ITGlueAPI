# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from itglue.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ORGANIZATION_TYPES = "/organization_types"
    ORGANIZATION_TYPES_ID = "/organization_types/{id}"
    ORGANIZATION_STATUSES = "/organization_statuses"
    ORGANIZATION_STATUSES_ID = "/organization_statuses/{id}"
    ORGANIZATIONS = "/organizations"
    ORGANIZATIONS_ID = "/organizations/{id}"
