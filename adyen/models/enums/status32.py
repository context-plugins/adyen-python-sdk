from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status32(str, Enum):
    """The status of the check.

    Possible values: **AWAITING_DATA** , **DATA_PROVIDED**, **FAILED**, **INVALID_DATA**, **PASSED**, **PENDING**,
    **RETRY_LIMIT_REACHED**."""

    AWAITING_DATA = "AWAITING_DATA"
    DATA_PROVIDED = "DATA_PROVIDED"
    FAILED = "FAILED"
    INVALID_DATA = "INVALID_DATA"
    PASSED = "PASSED"
    PENDING = "PENDING"
    PENDING_REVIEW = "PENDING_REVIEW"
    RETRY_LIMIT_REACHED = "RETRY_LIMIT_REACHED"
    UNCHECKED = "UNCHECKED"

    __str__ = str.__str__


Status32OrStr: TypeAlias = Annotated[Status32 | str, open_enum_validator(Status32)]
