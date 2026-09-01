from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentResponse1(SdkBaseModel):
    """Details about the payment method used in the transaction. Only returned if ``resultCode`` is **Authorised**."""

    brand: Optional[str] = UNSET
    """The card brand that the shopper used to pay. Only returned if ``paymentMethod.type`` is **scheme**."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The ``paymentMethod.type`` value used in the request."""


class PaymentResponse1Dict(TypedDict):
    brand: NotRequired[str]
    type_: NotRequired[str]
