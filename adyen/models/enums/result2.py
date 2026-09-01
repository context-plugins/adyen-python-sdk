from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Result2(str, Enum):
    """The result of this operation."""

    ACTIVE_RECURRING_TOKEN_EXISTS = "ACTIVE_RECURRING_TOKEN_EXISTS"
    ALREADY_PROCESSED = "ALREADY_PROCESSED"
    PAYMENT_NOT_FOUND = "PAYMENT_NOT_FOUND"
    SUCCESS = "SUCCESS"

    __str__ = str.__str__


Result2OrStr: TypeAlias = Annotated[Result2 | str, open_enum_validator(Result2)]
