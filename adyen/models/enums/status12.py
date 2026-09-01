from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status12(str, Enum):
    """The status of the account holder. >Permitted values: ``Active``, ``Inactive``, ``Suspended``, ``Closed``."""

    ACTIVE = "Active"
    CLOSED = "Closed"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"

    __str__ = str.__str__


Status12OrStr: TypeAlias = Annotated[Status12 | str, open_enum_validator(Status12)]
