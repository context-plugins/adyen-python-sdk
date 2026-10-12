from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CheckoutThreeDs2Action(SdkBaseModel):
    authorisation_token: Optional[str] = Field(default=UNSET, alias="authorisationToken")
    """A token needed to authorise a payment."""

    payment_data: Optional[str] = Field(default=UNSET, alias="paymentData")
    """Encoded payment data."""

    payment_method_type: Optional[str] = Field(default=UNSET, alias="paymentMethodType")
    """Specifies the payment method."""

    subtype: Optional[str] = UNSET
    """A subtype of the token."""

    token: Optional[str] = UNSET
    """A token to pass to the 3DS2 Component to get the fingerprint."""

    type_: Literal["threeDS2"] = Field(default="threeDS2", alias="type")
    """**threeDS2**"""

    url: Optional[str] = UNSET
    """Specifies the URL to redirect to."""


class CheckoutThreeDs2ActionDict(TypedDict):
    authorisation_token: NotRequired[str]
    payment_data: NotRequired[str]
    payment_method_type: NotRequired[str]
    subtype: NotRequired[str]
    token: NotRequired[str]
    type_: Literal["threeDS2"]
    url: NotRequired[str]
