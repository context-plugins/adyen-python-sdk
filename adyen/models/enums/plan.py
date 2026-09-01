from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Plan(str, Enum):
    """The installment plan, used for `card installments in Japan
    <https://docs.adyen.com/payment-methods/cards/credit-card-installments#make-a-payment-japan>`__. and `Mexico
    <https://docs.adyen.com/payment-methods/cards/credit-card-installments/#getting-paid-mexico>`__. By default, this is
    set to **regular**."""

    BONUS = "bonus"
    BUYNOW_PAYLATER = "buynow_paylater"
    INTERES_REFUND_PRCTG = "interes_refund_prctg"
    INTEREST_BONUS = "interest_bonus"
    NOINTERES_REFUND_PRCTG = "nointeres_refund_prctg"
    NOINTEREST_BONUS = "nointerest_bonus"
    REFUND_PRCTG = "refund_prctg"
    REGULAR = "regular"
    REVOLVING = "revolving"
    WITH_INTEREST = "with_interest"

    __str__ = str.__str__


PlanOrStr: TypeAlias = Annotated[Plan | str, open_enum_validator(Plan)]
