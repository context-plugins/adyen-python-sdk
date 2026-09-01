from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MainSourceOfIncome(str, Enum):
    """The organization's main source of income. Only required if ``businessType`` is **other**.

    Possible values: **businessOperation**, **realEstateSales**, **investmentInterestOrRoyalty**, **propertyRental**,
    **other**."""

    BUSINESS_OPERATION = "businessOperation"
    REAL_ESTATE_SALES = "realEstateSales"
    INVESTMENT_INTEREST_OR_ROYALTY = "investmentInterestOrRoyalty"
    PROPERTY_RENTAL = "propertyRental"
    OTHER = "other"

    __str__ = str.__str__


MainSourceOfIncomeOrStr: TypeAlias = Annotated[MainSourceOfIncome | str, open_enum_validator(MainSourceOfIncome)]
