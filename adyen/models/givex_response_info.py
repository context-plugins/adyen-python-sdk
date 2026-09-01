from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GivexResponseInfo(SdkBaseModel):
    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    """The three-character ISO currency code"""

    password: Optional[str] = UNSET
    """The password provided by the acquirer."""

    payment_flow: Optional[str] = Field(default=UNSET, alias="paymentFlow")
    """The sales channel used for the payment."""

    username: Optional[str] = UNSET
    """The username provided by the acquirer."""


class GivexResponseInfoDict(TypedDict):
    currency_code: NotRequired[str]
    password: NotRequired[str]
    payment_flow: NotRequired[str]
    username: NotRequired[str]
