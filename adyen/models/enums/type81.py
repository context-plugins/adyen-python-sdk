from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type81(str, Enum):
    """Type of terminal action: Uninstall an Android certificate."""

    UNINSTALL_ANDROID_CERTIFICATE = "UninstallAndroidCertificate"

    __str__ = str.__str__


Type81OrStr: TypeAlias = Annotated[Type81 | str, open_enum_validator(Type81)]
