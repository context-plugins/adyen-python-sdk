from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type38 import Type38OrStr


class Molpay(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    issuer: str
    """The shopper's bank. Specify this with the issuer value that corresponds to this bank."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    type_: Type38OrStr = Field(alias="type")
    """**molpay**"""


class MolpayDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    issuer: str
    sdk_data: NotRequired[str]
    type_: Type38OrStr
