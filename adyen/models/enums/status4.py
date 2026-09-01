from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status4(str, Enum):
    """The status of the request. This indicates whether the order was successfully updated with PayPal."""

    ERROR = "error"
    SUCCESS = "success"

    __str__ = str.__str__


Status4OrStr: TypeAlias = Annotated[Status4 | str, open_enum_validator(Status4)]
