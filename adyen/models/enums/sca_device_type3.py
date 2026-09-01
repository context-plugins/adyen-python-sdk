from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScaDeviceType3(str, Enum):
    """The type of the device."""

    BROWSER = "browser"
    IOS = "ios"
    ANDROID = "android"

    __str__ = str.__str__


ScaDeviceType3OrStr: TypeAlias = Annotated[ScaDeviceType3 | str, open_enum_validator(ScaDeviceType3)]
