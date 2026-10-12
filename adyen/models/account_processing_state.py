from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict


class AccountProcessingState(SdkBaseModel):
    disable_reason: Optional[str] = Field(default=UNSET, alias="disableReason")
    """The reason why processing has been disabled."""

    disabled: Optional[bool] = UNSET
    """Indicates whether the processing of payments is allowed."""

    processed_from: Optional[Amount] = Field(default=UNSET, alias="processedFrom")
    """The lower bound of the processing tier (i.e., an account holder must have processed at least this amount of money
    in order to be placed into this tier)."""

    processed_to: Optional[Amount] = Field(default=UNSET, alias="processedTo")
    """The upper bound of the processing tier (i.e., an account holder must have processed less than this amount of
    money in order to be placed into this tier)."""

    tier_number: Optional[int] = Field(default=UNSET, alias="tierNumber")
    """The processing tier that the account holder occupies."""


class AccountProcessingStateDict(TypedDict):
    disable_reason: NotRequired[str]
    disabled: NotRequired[bool]
    processed_from: NotRequired[AmountDict]
    processed_to: NotRequired[AmountDict]
    tier_number: NotRequired[int]
