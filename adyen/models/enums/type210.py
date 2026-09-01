from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type210(str, Enum):
    """The type of terminal action. The value **ForceReboot** triggers an immediate reboot of the specified
    terminal(s)."""

    FORCE_REBOOT = "ForceReboot"

    __str__ = str.__str__


Type210OrStr: TypeAlias = Annotated[Type210 | str, open_enum_validator(Type210)]
