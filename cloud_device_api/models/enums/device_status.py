from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeviceStatus(str, Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"

    __str__ = str.__str__


DeviceStatusOrStr: TypeAlias = Annotated[DeviceStatus | str, open_enum_validator(DeviceStatus)]
