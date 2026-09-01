from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type71(str, Enum):
    """Type of terminal action: Uninstall an Android app."""

    UNINSTALL_ANDROID_APP = "UninstallAndroidApp"

    __str__ = str.__str__


Type71OrStr: TypeAlias = Annotated[Type71 | str, open_enum_validator(Type71)]
