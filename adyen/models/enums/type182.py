from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type182(str, Enum):
    """The type of legal entity.

    Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**."""

    INDIVIDUAL = "individual"
    ORGANIZATION = "organization"
    SOLE_PROPRIETORSHIP = "soleProprietorship"
    TRUST = "trust"
    UNINCORPORATED_PARTNERSHIP = "unincorporatedPartnership"

    __str__ = str.__str__


Type182OrStr: TypeAlias = Annotated[Type182 | str, open_enum_validator(Type182)]
