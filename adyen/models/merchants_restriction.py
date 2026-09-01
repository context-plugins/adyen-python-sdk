from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .merchant_acquirer_pair import MerchantAcquirerPair, MerchantAcquirerPairDict


class MerchantsRestriction(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[MerchantAcquirerPair]] = UNSET
    """List of merchant ID and acquirer ID pairs."""


class MerchantsRestrictionDict(TypedDict):
    operation: str
    value: NotRequired[list[MerchantAcquirerPair | MerchantAcquirerPairDict]]
