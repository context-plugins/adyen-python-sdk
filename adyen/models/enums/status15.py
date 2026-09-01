from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status15(str, Enum):
    """The status of the transfer.

    Possible values:

     - **credited**: the funds are credited to your user's transfer instrument or bank account.- **accepted**: the
            request is accepted by the integration."""

    CREDITED = "credited"
    ACCEPTED = "accepted"

    __str__ = str.__str__


Status15OrStr: TypeAlias = Annotated[Status15 | str, open_enum_validator(Status15)]
