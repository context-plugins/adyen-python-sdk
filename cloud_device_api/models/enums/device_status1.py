from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeviceStatus1(str, Enum):
    """Indicates if the device has an active cloud connection. Possible values:
    * **ONLINE**
    * **OFFLINE**"""

    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"

    __str__ = str.__str__


DeviceStatus1OrStr: TypeAlias = Annotated[DeviceStatus1 | str, open_enum_validator(DeviceStatus1)]
