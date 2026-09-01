from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type112(str, Enum):
    """The type of entity that owns the bank account or card.

    Possible values: **individual**, **organization**, or **unknown**.

    Required when ``category`` is **card**. In this case, the value must be **individual**."""

    INDIVIDUAL = "individual"
    ORGANIZATION = "organization"
    UNKNOWN = "unknown"

    __str__ = str.__str__


Type112OrStr: TypeAlias = Annotated[Type112 | str, open_enum_validator(Type112)]
