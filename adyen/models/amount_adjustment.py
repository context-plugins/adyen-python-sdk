from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .enums.amount_adjustment_type import AmountAdjustmentTypeOrStr


class AmountAdjustment(SdkBaseModel):
    amount: Optional[Amount17] = UNSET
    """The adjustment amount."""

    amount_adjustment_type: Optional[AmountAdjustmentTypeOrStr] = Field(default=UNSET, alias="amountAdjustmentType")
    """The type of markup that is applied to an authorised payment.

    Possible values: **exchange**, **forexMarkup**, **authHoldReserve**, **atmMarkup**."""

    basepoints: Optional[int] = UNSET
    """The basepoints associated with the applied markup."""


class AmountAdjustmentDict(TypedDict):
    amount: NotRequired[Amount17Dict]
    amount_adjustment_type: NotRequired[AmountAdjustmentTypeOrStr]
    basepoints: NotRequired[int]
