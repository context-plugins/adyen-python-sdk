from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LegalEntityType(str, Enum):
    """The legal entity type.

    Possible values: **Business**, **Individual**, **NonProfit**, **PublicCompany**, or **Partnership**."""

    BUSINESS = "Business"
    INDIVIDUAL = "Individual"
    NON_PROFIT = "NonProfit"
    PARTNERSHIP = "Partnership"
    PUBLIC_COMPANY = "PublicCompany"

    __str__ = str.__str__


LegalEntityTypeOrStr: TypeAlias = Annotated[LegalEntityType | str, open_enum_validator(LegalEntityType)]
