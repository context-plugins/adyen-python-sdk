from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LegalEntity(str, Enum):
    """The legal entity type of the account holder. This determines the information that should be provided in the
    request.

    Possible values: **Business**, **Individual**, or **NonProfit**.

    * If set to **Business** or **NonProfit**, then ``accountHolderDetails.businessDetails`` must be provided, with at
        least one entry in the ``accountHolderDetails.businessDetails.shareholders`` list.

    * If set to **Individual**, then ``accountHolderDetails.individualDetails`` must be provided."""

    BUSINESS = "Business"
    INDIVIDUAL = "Individual"
    NON_PROFIT = "NonProfit"
    PARTNERSHIP = "Partnership"
    PUBLIC_COMPANY = "PublicCompany"

    __str__ = str.__str__


LegalEntityOrStr: TypeAlias = Annotated[LegalEntity | str, open_enum_validator(LegalEntity)]
