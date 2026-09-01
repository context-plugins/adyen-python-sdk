from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.event import EventOrStr


class AccountEvent(SdkBaseModel):
    event: Optional[EventOrStr] = UNSET
    """The event. >Permitted values: ``InactivateAccount``, ``RefundNotPaidOutTransfers``. For more information, refer
    to `Verification checks <https://docs.adyen.com/classic-platforms/verification-process>`__."""

    execution_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="executionDate")
    """The date on which the event will take place."""

    reason: Optional[str] = UNSET
    """The reason why this event has been created."""


class AccountEventDict(TypedDict):
    event: NotRequired[EventOrStr]
    execution_date: NotRequired[RFC3339DateTime]
    reason: NotRequired[str]
