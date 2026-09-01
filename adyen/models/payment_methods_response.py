from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment_method import PaymentMethod, PaymentMethodDict
from .stored_payment_method3 import StoredPaymentMethod3, StoredPaymentMethod3Dict


class PaymentMethodsResponse(SdkBaseModel):
    payment_methods: Optional[list[PaymentMethod]] = Field(default=UNSET, alias="paymentMethods")
    """Detailed list of payment methods required to generate payment forms."""

    stored_payment_methods: Optional[list[StoredPaymentMethod3]] = Field(default=UNSET, alias="storedPaymentMethods")
    """List of all stored payment methods."""


class PaymentMethodsResponseDict(TypedDict):
    payment_methods: NotRequired[list[PaymentMethod | PaymentMethodDict]]
    stored_payment_methods: NotRequired[list[StoredPaymentMethod3 | StoredPaymentMethod3Dict]]
