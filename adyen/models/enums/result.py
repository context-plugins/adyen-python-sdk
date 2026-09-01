from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Result(str, Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    UNKNOWN = "UNKNOWN"
    NOT_REQUIRED = "NOT_REQUIRED"

    __str__ = str.__str__


ResultOrStr: TypeAlias = Annotated[Result | str, open_enum_validator(Result)]
