from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fee_type import FeeTypeOrStr
from .enums.type3 import Type3OrStr


class Alma(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    fee_type: Optional[FeeTypeOrStr] = Field(default=UNSET, alias="feeType")
    """**Alma payment request fee type**"""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    type_: Optional[Type3OrStr] = Field(default=UNSET, alias="type")
    """The payment method type."""


class AlmaDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    fee_type: NotRequired[FeeTypeOrStr]
    sdk_data: NotRequired[str]
    type_: NotRequired[Type3OrStr]
