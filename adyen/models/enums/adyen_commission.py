from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdyenCommission(str, Enum):
    """Deducts the transaction fee due to Adyen under `blended rates
    <https://www.adyen.com/knowledge-hub/guides/payments-training-guide/get-the-best-from-your-card-processing>`__ from
    the specified balance account.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**."""

    DEDUCT_FROM_LIABLE_ACCOUNT = "deductFromLiableAccount"
    DEDUCT_FROM_ONE_BALANCE_ACCOUNT = "deductFromOneBalanceAccount"

    __str__ = str.__str__


AdyenCommissionOrStr: TypeAlias = Annotated[AdyenCommission | str, open_enum_validator(AdyenCommission)]
