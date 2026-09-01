from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageClass(str, Enum):
    """Possible values:
    * **Service**
    * **Device**
    * **Event**"""

    SERVICE = "Service"
    DEVICE = "Device"
    EVENT = "Event"

    __str__ = str.__str__


MessageClassOrStr: TypeAlias = Annotated[MessageClass | str, open_enum_validator(MessageClass)]
