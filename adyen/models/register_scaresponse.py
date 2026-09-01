from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RegisterScaresponse(SdkBaseModel):
    id: Optional[str] = UNSET
    """The unique identifier of the SCA device you are registering."""

    payment_instrument_id: Optional[str] = Field(default=UNSET, alias="paymentInstrumentId")
    """The unique identifier of the payment instrument for which you are registering the SCA device."""

    sdk_input: Optional[str] = Field(default=UNSET, alias="sdkInput")
    """A string that you must pass to the authentication SDK to continue with the registration process."""

    success: Optional[bool] = UNSET
    """Specifies if the registration was initiated successfully."""


class RegisterScaresponseDict(TypedDict):
    id: NotRequired[str]
    payment_instrument_id: NotRequired[str]
    sdk_input: NotRequired[str]
    success: NotRequired[bool]
