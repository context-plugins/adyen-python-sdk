from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status16(str, Enum):
    """The new status of the network token. Possible values: **active**, **suspended**, **closed**. The **closed**
    status is final and cannot be changed."""

    ACTIVE = "active"
    SUSPENDED = "suspended"
    CLOSED = "closed"

    __str__ = str.__str__


Status16OrStr: TypeAlias = Annotated[Status16 | str, open_enum_validator(Status16)]
