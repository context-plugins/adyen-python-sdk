from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status8(str, Enum):
    """The status of the store. Possible values: **Pending**, **Active**, **Inactive**, **InactiveWithModifications**,
    **Closed**."""

    ACTIVE = "Active"
    CLOSED = "Closed"
    INACTIVE = "Inactive"
    INACTIVE_WITH_MODIFICATIONS = "InactiveWithModifications"
    PENDING = "Pending"

    __str__ = str.__str__


Status8OrStr: TypeAlias = Annotated[Status8 | str, open_enum_validator(Status8)]
