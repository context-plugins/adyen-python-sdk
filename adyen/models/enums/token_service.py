from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TokenService(str, Enum):
    """The name of the token service."""

    VISATOKENSERVICE = "VISATOKENSERVICE"
    MCTOKENSERVICE = "MCTOKENSERVICE"
    AMEXTOKENSERVICE = "AMEXTOKENSERVICE"
    TOKEN_SHARING = "TOKEN_SHARING"

    __str__ = str.__str__


TokenServiceOrStr: TypeAlias = Annotated[TokenService | str, open_enum_validator(TokenService)]
