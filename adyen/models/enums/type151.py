from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type151(str, Enum):
    """The tax reporting classification type.

    Possible values: **nonFinancialNonReportable**, **financialNonReportable**, **nonFinancialActive**,
    **nonFinancialPassive**."""

    NON_FINANCIAL_NON_REPORTABLE = "nonFinancialNonReportable"
    FINANCIAL_NON_REPORTABLE = "financialNonReportable"
    NON_FINANCIAL_ACTIVE = "nonFinancialActive"
    NON_FINANCIAL_PASSIVE = "nonFinancialPassive"

    __str__ = str.__str__


Type151OrStr: TypeAlias = Annotated[Type151 | str, open_enum_validator(Type151)]
