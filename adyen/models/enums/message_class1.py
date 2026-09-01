from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageClass1(str, Enum):
    """Class of the message. Possible values:
    * **Device**
    * **Event**
    * **Service**"""

    SERVICE = "Service"
    DEVICE = "Device"
    EVENT = "Event"

    __str__ = str.__str__


MessageClass1OrStr: TypeAlias = Annotated[MessageClass1 | str, open_enum_validator(MessageClass1)]
