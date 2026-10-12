from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .message_reference3 import MessageReference3, MessageReference3Dict
from .repeated_message_response2 import RepeatedMessageResponse2, RepeatedMessageResponse2Dict
from .response11 import Response11, Response11Dict


class TransactionStatusResponse(SdkBaseModel):
    """Content of the TransactionStatus Response message. It conveys Information related to the status of the last or
    current Payment, Loyalty or Reversal transaction."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    message_reference: Optional[MessageReference3] = Field(default=UNSET, alias="MessageReference")
    """Identification of a previous POI transaction. If ``Response.Result`` is Success."""

    repeated_message_response: Optional[RepeatedMessageResponse2] = Field(
        default=UNSET, alias="RepeatedMessageResponse"
    )
    """Content of the requested Message Response. If Result is Success (process completed)."""


class TransactionStatusResponseDict(TypedDict):
    response: Response11Dict
    message_reference: NotRequired[MessageReference3Dict]
    repeated_message_response: NotRequired[RepeatedMessageResponse2Dict]
