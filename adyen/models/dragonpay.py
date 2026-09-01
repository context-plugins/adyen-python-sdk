from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type28 import Type28OrStr


class Dragonpay(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    issuer: str
    """The Dragonpay issuer value of the shopper's selected bank. Set this to an **id** of a Dragonpay issuer to
    preselect it."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The shopper’s email address."""

    type_: Type28OrStr = Field(alias="type")
    """**dragonpay**"""


class DragonpayDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    issuer: str
    sdk_data: NotRequired[str]
    shopper_email: NotRequired[str]
    type_: Type28OrStr
