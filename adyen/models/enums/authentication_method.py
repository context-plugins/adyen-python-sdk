from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AuthenticationMethod(str, Enum):
    """Allowed authentication methods: Magswipe, Manual Entry."""

    MAGSWIPE = "MAGSWIPE"
    MKE = "MKE"

    __str__ = str.__str__


AuthenticationMethodOrStr: TypeAlias = Annotated[AuthenticationMethod | str, open_enum_validator(AuthenticationMethod)]
