from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.plan1 import Plan1OrStr


class CheckoutSessionInstallmentOption(SdkBaseModel):
    plans: Optional[list[Plan1OrStr]] = UNSET
    """Defines the type of installment plan. If not set, defaults to **regular**.

    Possible values:
    * **regular**
    * **revolving**
    * **bonus**
    * **with_interest**
    * **buynow_paylater**
    * **nointerest_bonus**
    * **interest_bonus**
    * **refund_prctg**
    * **nointeres_refund_prctg**
    * **interes_refund_prctg**"""

    preselected_value: Optional[int] = Field(default=UNSET, alias="preselectedValue")
    """Preselected number of installments offered for this payment method."""

    values: Optional[list[int]] = UNSET
    """An array of the number of installments that the shopper can choose from. For example, **[2,3,5]**. This cannot be
    specified simultaneously with ``maxValue``."""


class CheckoutSessionInstallmentOptionDict(TypedDict):
    plans: NotRequired[list[Plan1OrStr]]
    preselected_value: NotRequired[int]
    values: NotRequired[list[int]]
