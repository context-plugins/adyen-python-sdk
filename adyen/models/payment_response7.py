from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment_validations_name_response2 import PaymentValidationsNameResponse2, PaymentValidationsNameResponse2Dict


class PaymentResponse7(SdkBaseModel):
    name: Optional[PaymentValidationsNameResponse2] = UNSET
    """Object that contains the status and outcomes of the `name validation
    <https://docs.adyen.com/payment-methods/cards/name-validation>`__."""


class PaymentResponse7Dict(TypedDict):
    name: NotRequired[PaymentValidationsNameResponse2Dict]
