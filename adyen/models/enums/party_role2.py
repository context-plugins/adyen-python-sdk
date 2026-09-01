from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartyRole2(str, Enum):
    """Specifies a role or capacity of the party in relation to the bank account."""

    HOLDER = "HOLDER"
    AUTHORIZED_USER = "AUTHORIZED_USER"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


PartyRole2OrStr: TypeAlias = Annotated[PartyRole2 | str, open_enum_validator(PartyRole2)]
