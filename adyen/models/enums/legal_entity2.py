from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LegalEntity2(str, Enum):
    """The legal entity of the account holder."""

    BUSINESS = "Business"
    INDIVIDUAL = "Individual"
    NON_PROFIT = "NonProfit"
    PARTNERSHIP = "Partnership"
    PUBLIC_COMPANY = "PublicCompany"

    __str__ = str.__str__


LegalEntity2OrStr: TypeAlias = Annotated[LegalEntity2 | str, open_enum_validator(LegalEntity2)]
