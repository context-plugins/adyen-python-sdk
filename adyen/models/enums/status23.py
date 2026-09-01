from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status23(str, Enum):
    """The status of the balance account, set to **active** by default."""

    ACTIVE = "active"
    CLOSED = "closed"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

    __str__ = str.__str__


Status23OrStr: TypeAlias = Annotated[Status23 | str, open_enum_validator(Status23)]
