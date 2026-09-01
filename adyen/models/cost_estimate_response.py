from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict
from .card_bin1 import CardBin1, CardBin1Dict


class CostEstimateResponse(SdkBaseModel):
    card_bin: Optional[CardBin1] = Field(default=UNSET, alias="cardBin")
    """Card BIN details."""

    cost_estimate_amount: Optional[Amount] = Field(default=UNSET, alias="costEstimateAmount")
    """The estimated cost (scheme fee + interchange) in the settlement currency. If the settlement currency cannot be
    determined, the fee in EUR is returned."""

    cost_estimate_reference: Optional[str] = Field(default=UNSET, alias="costEstimateReference")
    """Adyen's 16-character reference associated with the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result of the cost estimation."""


class CostEstimateResponseDict(TypedDict):
    card_bin: NotRequired[CardBin1 | CardBin1Dict]
    cost_estimate_amount: NotRequired[Amount | AmountDict]
    cost_estimate_reference: NotRequired[str]
    result_code: NotRequired[str]
