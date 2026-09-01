from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type12 import Type12OrStr


class BillDesk(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    issuer: str
    """The issuer id of the shopper's selected bank."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    type_: Type12OrStr = Field(alias="type")
    """**billdesk**"""


class BillDeskDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    issuer: str
    sdk_data: NotRequired[str]
    type_: Type12OrStr
