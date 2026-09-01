from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type39(str, Enum):
    """**openinvoice**"""

    OPENINVOICE = "openinvoice"
    AFTERPAY_DIRECTDEBIT = "afterpay_directdebit"
    ATOME_POS = "atome_pos"

    __str__ = str.__str__


Type39OrStr: TypeAlias = Annotated[Type39 | str, open_enum_validator(Type39)]
