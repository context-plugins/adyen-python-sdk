from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MerchantAcquirerPair(SdkBaseModel):
    acquirer_id: Optional[str] = Field(default=UNSET, alias="acquirerId")
    """The acquirer ID."""

    merchant_id: Optional[str] = Field(default=UNSET, alias="merchantId")
    """The merchant identification number (MID)."""


class MerchantAcquirerPairDict(TypedDict):
    acquirer_id: NotRequired[str]
    merchant_id: NotRequired[str]
