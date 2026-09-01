from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status43(str, Enum):
    """The status of the balance account. Payment instruments linked to the balance account can only be used if the
    balance account status is **active**.

    Possible values: **active**, **closed**, **suspended**."""

    ACTIVE = "active"
    CLOSED = "closed"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

    __str__ = str.__str__


Status43OrStr: TypeAlias = Annotated[Status43 | str, open_enum_validator(Status43)]
