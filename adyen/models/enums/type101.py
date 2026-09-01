from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type101(str, Enum):
    """The type of device.

    Possible values: **ios**, **android**, **browser**."""

    IOS = "ios"
    ANDROID = "android"
    BROWSER = "browser"

    __str__ = str.__str__


Type101OrStr: TypeAlias = Annotated[Type101 | str, open_enum_validator(Type101)]
