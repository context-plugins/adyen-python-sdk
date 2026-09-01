from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type61(str, Enum):
    """Type of terminal action: Update Release."""

    RELEASE_UPDATE = "ReleaseUpdate"

    __str__ = str.__str__


Type61OrStr: TypeAlias = Annotated[Type61 | str, open_enum_validator(Type61)]
