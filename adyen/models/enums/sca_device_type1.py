from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScaDeviceType1(str, Enum):
    """Type of device registered.

    Possible values: **ios**, **android**, **browser**."""

    BROWSER = "browser"
    IOS = "ios"
    ANDROID = "android"

    __str__ = str.__str__


ScaDeviceType1OrStr: TypeAlias = Annotated[ScaDeviceType1 | str, open_enum_validator(ScaDeviceType1)]
