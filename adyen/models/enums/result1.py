from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Result1(str, Enum):
    """Result of the validation. Ex: valid, invalid, unknown"""

    VALID = "VALID"
    INVALID = "INVALID"
    UNKNOWN = "UNKNOWN"
    NOT_REQUIRED = "NOT_REQUIRED"

    __str__ = str.__str__


Result1OrStr: TypeAlias = Annotated[Result1 | str, open_enum_validator(Result1)]
