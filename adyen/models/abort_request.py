from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .display_output1 import DisplayOutput1, DisplayOutput1Dict
from .message_reference4 import MessageReference4, MessageReference4Dict


class AbortRequest(SdkBaseModel):
    """Body of the Abort Request message. It conveys Information requested for identification of the message request
    carrying the transaction to abort. A message to display on the CustomerError Device could be sent by the Sale System
    (DisplayOutput)."""

    message_reference: MessageReference4 = Field(alias="MessageReference")
    """Identification of a previous POI transaction."""

    abort_reason: str = Field(alias="AbortReason")
    """Reason of aborting a transaction."""

    display_output: Optional[DisplayOutput1] = Field(default=UNSET, alias="DisplayOutput")
    """Information to display and the way to process the display. To display an abort message to the Customer."""


class AbortRequestDict(TypedDict):
    message_reference: MessageReference4Dict
    abort_reason: str
    display_output: NotRequired[DisplayOutput1Dict]
