from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NetworkType2(str, Enum):
    """Network type for Terminal API details webhooks."""

    LOCAL = "local"
    PUBLIC = "public"

    __str__ = str.__str__


NetworkType2OrStr: TypeAlias = Annotated[NetworkType2 | str, open_enum_validator(NetworkType2)]
