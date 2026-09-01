from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayoutScheduleExecutionDetails(SdkBaseModel):
    reason: Optional[str] = UNSET
    """Human readable reason for why execution was not successful if applicable."""

    reason_code: Optional[str] = Field(default=UNSET, alias="reasonCode")
    """Reason Code for why execution was not successful if applicable."""

    transfer_id: Optional[str] = Field(default=UNSET, alias="transferId")
    """The id of the transfer from executing the payout."""


class PayoutScheduleExecutionDetailsDict(TypedDict):
    reason: NotRequired[str]
    reason_code: NotRequired[str]
    transfer_id: NotRequired[str]
