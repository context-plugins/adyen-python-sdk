from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdyenMarkup(str, Enum):
    """Deducts the transaction fee due to Adyen under `Interchange ++ pricing
    <https://www.adyen.com/what-is-interchange>`__ from the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    DEDUCT_FROM_LIABLE_ACCOUNT = "deductFromLiableAccount"
    DEDUCT_FROM_ONE_BALANCE_ACCOUNT = "deductFromOneBalanceAccount"

    __str__ = str.__str__


AdyenMarkupOrStr: TypeAlias = Annotated[AdyenMarkup | str, open_enum_validator(AdyenMarkup)]
