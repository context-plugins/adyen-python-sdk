from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.plan import PlanOrStr


class Installments(SdkBaseModel):
    """Contains installment settings. For more information, refer to `Installments
    <https://docs.adyen.com/payment-methods/cards/credit-card-installments>`__."""

    extra: Optional[int] = UNSET
    """Defines the bonus percentage, refund percentage or if the transaction is Buy now Pay later. Used for `card
    installments in Mexico
    <https://docs.adyen.com/payment-methods/cards/credit-card-installments/#getting-paid-mexico>`__"""

    plan: Optional[PlanOrStr] = UNSET
    """The installment plan, used for `card installments in Japan
    <https://docs.adyen.com/payment-methods/cards/credit-card-installments#make-a-payment-japan>`__. and `Mexico
    <https://docs.adyen.com/payment-methods/cards/credit-card-installments/#getting-paid-mexico>`__. By default, this is
    set to **regular**."""

    value: int
    """Defines the number of installments. Usually, the maximum allowed number of installments is capped. For example,
    it may not be possible to split a payment in more than 24 installments. The acquirer sets this upper limit, so its
    value may vary. This value can be zero for Installments processed in Mexico."""


class InstallmentsDict(TypedDict):
    extra: NotRequired[int]
    plan: NotRequired[PlanOrStr]
    value: int
