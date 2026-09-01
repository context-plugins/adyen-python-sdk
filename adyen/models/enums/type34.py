from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type34(str, Enum):
    """**klarna**"""

    KLARNA = "klarna"
    KLARNAPAYMENTS = "klarnapayments"
    KLARNAPAYMENTS_ACCOUNT = "klarnapayments_account"
    KLARNAPAYMENTS_B2B = "klarnapayments_b2b"
    KLARNA_PAYNOW = "klarna_paynow"
    KLARNA_ACCOUNT = "klarna_account"
    KLARNA_B2B = "klarna_b2b"

    __str__ = str.__str__


Type34OrStr: TypeAlias = Annotated[Type34 | str, open_enum_validator(Type34)]
