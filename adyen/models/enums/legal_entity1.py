from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LegalEntity1(str, Enum):
    """The type of legal entity of the new account holder."""

    BUSINESS = "Business"
    INDIVIDUAL = "Individual"
    NON_PROFIT = "NonProfit"
    PARTNERSHIP = "Partnership"
    PUBLIC_COMPANY = "PublicCompany"

    __str__ = str.__str__


LegalEntity1OrStr: TypeAlias = Annotated[LegalEntity1 | str, open_enum_validator(LegalEntity1)]
