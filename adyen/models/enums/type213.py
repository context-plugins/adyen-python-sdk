from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type213(str, Enum):
    """The type of legal entity.

     Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**."""

    INDIVIDUAL = "individual"
    ORGANIZATION = "organization"
    SOLE_PROPRIETORSHIP = "soleProprietorship"
    TRUST = "trust"
    UNINCORPORATED_PARTNERSHIP = "unincorporatedPartnership"

    __str__ = str.__str__


Type213OrStr: TypeAlias = Annotated[Type213 | str, open_enum_validator(Type213)]
