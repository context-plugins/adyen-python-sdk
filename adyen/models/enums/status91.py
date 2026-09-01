from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status91(str, Enum):
    """The status of the network token. Possible values: **active**, **inactive**, **suspended**, **closed**."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    CLOSED = "closed"

    __str__ = str.__str__


Status91OrStr: TypeAlias = Annotated[Status91 | str, open_enum_validator(Status91)]
