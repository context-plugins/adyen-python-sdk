from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status42(str, Enum):
    """The status of the account. >Permitted values: ``Active``."""

    ACTIVE = "Active"
    CLOSED = "Closed"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"

    __str__ = str.__str__


Status42OrStr: TypeAlias = Annotated[Status42 | str, open_enum_validator(Status42)]
