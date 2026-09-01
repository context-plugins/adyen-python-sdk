from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status44(str, Enum):
    """The status of the transfer.

    Possible values:

     - **pending**: the transfer is under internal review by Adyen.

    - **failed**: the transfer failed Adyen's internal review. For details, see ``reason``."""

    PENDING = "pending"
    FAILED = "failed"

    __str__ = str.__str__


Status44OrStr: TypeAlias = Annotated[Status44 | str, open_enum_validator(Status44)]
