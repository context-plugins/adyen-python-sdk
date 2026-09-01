from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TicketInfo2(SdkBaseModel):
    """Details to provide if ``type`` is **ticket** (Edenred Brazil)."""

    requestor_id: Optional[str] = Field(default=UNSET, alias="requestorId")
    """Ticket requestorId"""


class TicketInfo2Dict(TypedDict):
    requestor_id: NotRequired[str]
