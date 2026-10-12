from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status import StatusOrStr
from .payment_validations_name_result_raw_response2 import (
    PaymentValidationsNameResultRawResponse2,
    PaymentValidationsNameResultRawResponse2Dict,
)
from .payment_validations_name_result_response2 import (
    PaymentValidationsNameResultResponse2,
    PaymentValidationsNameResultResponse2Dict,
)


class PaymentValidationsNameResponse2(SdkBaseModel):
    """Object that contains the status and outcomes of the `name validation
    <https://docs.adyen.com/payment-methods/cards/name-validation>`__."""

    raw_response: Optional[PaymentValidationsNameResultRawResponse2] = Field(default=UNSET, alias="rawResponse")
    """Contains the raw response(s) returned by the scheme for the name validation."""

    result: Optional[PaymentValidationsNameResultResponse2] = UNSET
    """Contains the scheme-agnostic match values returned by Adyen."""

    status: Optional[StatusOrStr] = UNSET
    """Informs you if the name validation was performed. Possible values:

    **performed**, **notPerformed**, **notSupported**"""


class PaymentValidationsNameResponse2Dict(TypedDict):
    raw_response: NotRequired[PaymentValidationsNameResultRawResponse2Dict]
    result: NotRequired[PaymentValidationsNameResultResponse2Dict]
    status: NotRequired[StatusOrStr]
