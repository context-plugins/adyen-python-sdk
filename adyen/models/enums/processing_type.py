from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProcessingType(str, Enum):
    """The type of transactions processed over this payment method.
     Allowed values:
    - **pos** for in-person payments.
    - **billpay** for subscription payments, both the initial payment and the later recurring payments. These
        transactions have ``recurringProcessingModel`` **Subscription**.
    - **ecom** for all other card not present transactions. This includes non-recurring transactions and transactions
        with ``recurringProcessingModel`` **CardOnFile** or **UnscheduledCardOnFile**."""

    BILLPAY = "billpay"
    ECOM = "ecom"
    POS = "pos"

    __str__ = str.__str__


ProcessingTypeOrStr: TypeAlias = Annotated[ProcessingType | str, open_enum_validator(ProcessingType)]
