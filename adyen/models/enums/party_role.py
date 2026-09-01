from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartyRole(str, Enum):
    HOLDER = "HOLDER"
    AUTHORIZED_USER = "AUTHORIZED_USER"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


PartyRoleOrStr: TypeAlias = Annotated[PartyRole | str, open_enum_validator(PartyRole)]
