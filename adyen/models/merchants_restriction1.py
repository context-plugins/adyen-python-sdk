from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .merchant_acquirer_pair import MerchantAcquirerPair, MerchantAcquirerPairDict


class MerchantsRestriction1(SdkBaseModel):
    """List of merchant ID and acquirer ID pairs, and the operation.

    Supported operations: **anyMatch**, **noneMatch**."""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[MerchantAcquirerPair]] = UNSET
    """List of merchant ID and acquirer ID pairs."""


class MerchantsRestriction1Dict(TypedDict):
    operation: str
    value: NotRequired[list[MerchantAcquirerPair | MerchantAcquirerPairDict]]
