from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type46 import Type46OrStr


class PseLatam(SdkBaseModel):
    bank: str
    """The shopper's bank."""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    client_type: str = Field(alias="clientType")
    """The client type."""

    identification: str
    """The identification code."""

    identification_type: str = Field(alias="identificationType")
    """The identification type."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    type_: Optional[Type46OrStr] = Field(default=UNSET, alias="type")
    """The payment method type."""


class PseLatamDict(TypedDict):
    bank: str
    checkout_attempt_id: NotRequired[str]
    client_type: str
    identification: str
    identification_type: str
    sdk_data: NotRequired[str]
    type_: NotRequired[Type46OrStr]
