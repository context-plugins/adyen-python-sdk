from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status14(str, Enum):
    """The current status of the grant. Possible values: **Pending**, **Active**, **Repaid**, **WrittenOff**,
    **Failed**, **Revoked**."""

    PENDING = "Pending"
    ACTIVE = "Active"
    REPAID = "Repaid"
    FAILED = "Failed"
    WRITTEN_OFF = "WrittenOff"
    REVOKED = "Revoked"

    __str__ = str.__str__


Status14OrStr: TypeAlias = Annotated[Status14 | str, open_enum_validator(Status14)]
