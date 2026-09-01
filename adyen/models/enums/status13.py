from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status13(str, Enum):
    """The status of the request for PIN change.

    Possible values: **completed**, **pending**, **unavailable**."""

    COMPLETED = "completed"
    PENDING = "pending"
    UNAVAILABLE = "unavailable"

    __str__ = str.__str__


Status13OrStr: TypeAlias = Annotated[Status13 | str, open_enum_validator(Status13)]
