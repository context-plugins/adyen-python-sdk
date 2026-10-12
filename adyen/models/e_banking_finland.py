from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EBankingFinland(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    issuer: Optional[str] = UNSET
    """The Ebanking Finland issuer value of the shopper's selected bank."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    type_: Literal["ebanking_FI"] = Field(default="ebanking_FI", alias="type")
    """**ebanking_FI**"""


class EBankingFinlandDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    issuer: NotRequired[str]
    sdk_data: NotRequired[str]
    type_: Literal["ebanking_FI"]
