from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TicketInfo(SdkBaseModel):
    requestor_id: Optional[str] = Field(default=UNSET, alias="requestorId")
    """Ticket requestorId"""


class TicketInfoDict(TypedDict):
    requestor_id: NotRequired[str]
