from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransactionType(str, Enum):
    """Identify the type of the transaction being authenticated."""

    GOODS_OR_SERVICE_PURCHASE = "goodsOrServicePurchase"
    CHECK_ACCEPTANCE = "checkAcceptance"
    ACCOUNT_FUNDING = "accountFunding"
    QUASI_CASH_TRANSACTION = "quasiCashTransaction"
    PREPAID_ACTIVATION_AND_LOAD = "prepaidActivationAndLoad"

    __str__ = str.__str__


TransactionTypeOrStr: TypeAlias = Annotated[TransactionType | str, open_enum_validator(TransactionType)]
