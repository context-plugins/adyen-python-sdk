from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status22(str, Enum):
    """The new status of the account. >Permitted values: ``Active``, ``Inactive``, ``Suspended``, ``Closed``."""

    ACTIVE = "Active"
    CLOSED = "Closed"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"

    __str__ = str.__str__


Status22OrStr: TypeAlias = Annotated[Status22 | str, open_enum_validator(Status22)]
