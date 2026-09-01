from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status71(str, Enum):
    """The status of the PIN delivery."""

    CREATED = "created"
    DELIVERED = "delivered"
    NOT_APPLICABLE = "notApplicable"
    PROCESSING = "processing"
    PRODUCED = "produced"
    REJECTED = "rejected"
    SHIPPED = "shipped"
    UNKNOWN = "unknown"

    __str__ = str.__str__


Status71OrStr: TypeAlias = Annotated[Status71 | str, open_enum_validator(Status71)]
