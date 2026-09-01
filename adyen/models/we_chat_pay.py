from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type56 import Type56OrStr


class WeChatPay(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    type_: Optional[Type56OrStr] = Field(default=UNSET, alias="type")
    """**wechatpay**"""


class WeChatPayDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    sdk_data: NotRequired[str]
    type_: NotRequired[Type56OrStr]
