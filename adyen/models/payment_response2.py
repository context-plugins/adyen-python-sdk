from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment_validations_name_response2 import PaymentValidationsNameResponse2, PaymentValidationsNameResponse2Dict


class PaymentResponse2(SdkBaseModel):
    """The object that contains the validation outcomes. Only returned if ``resultCode`` is **Authorised** and if you
    have requested a payment validation in the request."""

    name: Optional[PaymentValidationsNameResponse2] = UNSET
    """Object that contains the status and outcomes of the `name validation
    <https://docs.adyen.com/payment-methods/cards/name-validation>`__."""


class PaymentResponse2Dict(TypedDict):
    name: NotRequired[PaymentValidationsNameResponse2 | PaymentValidationsNameResponse2Dict]
