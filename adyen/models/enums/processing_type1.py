from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProcessingType1(str, Enum):
    """Contains information about how the payment was processed.

    Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **purchaseWithCashback**,
    **recurring**, **token**."""

    ATM_WITHDRAW = "atmWithdraw"
    BALANCE_INQUIRY = "balanceInquiry"
    ECOMMERCE = "ecommerce"
    MOTO = "moto"
    POS = "pos"
    PURCHASE_WITH_CASHBACK = "purchaseWithCashback"
    RECURRING = "recurring"
    TOKEN = "token"

    __str__ = str.__str__


ProcessingType1OrStr: TypeAlias = Annotated[ProcessingType1 | str, open_enum_validator(ProcessingType1)]
