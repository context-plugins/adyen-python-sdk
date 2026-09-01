from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type32(str, Enum):
    """Type of terminal action: Install an Android app."""

    INSTALL_ANDROID_APP = "InstallAndroidApp"

    __str__ = str.__str__


Type32OrStr: TypeAlias = Annotated[Type32 | str, open_enum_validator(Type32)]
