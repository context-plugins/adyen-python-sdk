from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TicketResponseInfo2(SdkBaseModel):
    """**ticket** (Edenred Brazil) details"""

    requestor_id: Optional[str] = Field(default=UNSET, alias="requestorId")
    """Ticket requestorId"""


class TicketResponseInfo2Dict(TypedDict):
    requestor_id: NotRequired[str]
