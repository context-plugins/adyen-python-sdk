from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScaDeviceType(str, Enum):
    BROWSER = "browser"
    IOS = "ios"
    ANDROID = "android"

    __str__ = str.__str__


ScaDeviceTypeOrStr: TypeAlias = Annotated[ScaDeviceType | str, open_enum_validator(ScaDeviceType)]
