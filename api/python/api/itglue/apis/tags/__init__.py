# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from itglue.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ORGANIZATIONS = "Organizations"
    ORGANIZATION_TYPES = "Organization Types"
    ORGANIZATION_STATUSES = "Organization Statuses"
    DEFAULT = "default"
