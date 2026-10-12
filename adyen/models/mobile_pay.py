from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type37 import Type37, Type37OrStr


class MobilePay(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    type_: Type37OrStr = Field(default=Type37.MOBILEPAY, alias="type")
    """**mobilepay**"""


class MobilePayDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    sdk_data: NotRequired[str]
    type_: NotRequired[Type37OrStr]
