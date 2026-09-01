from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status62(str, Enum):
    """The resulting status of the return.

    Possible values: **Authorised**, **Declined**."""

    AUTHORISED = "Authorised"
    DECLINED = "Declined"

    __str__ = str.__str__


Status62OrStr: TypeAlias = Annotated[Status62 | str, open_enum_validator(Status62)]
