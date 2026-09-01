from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .message_header import MessageHeader, MessageHeaderDict
from .repeated_response_message_body import RepeatedResponseMessageBody, RepeatedResponseMessageBodyDict


class RepeatedMessageResponse(SdkBaseModel):
    message_header: MessageHeader = Field(alias="MessageHeader")
    """Message header of the Sale to POI protocol message. It conveys Information related to the Sale to POI protocol
    management."""

    repeated_response_message_body: RepeatedResponseMessageBody = Field(alias="RepeatedResponseMessageBody")


class RepeatedMessageResponseDict(TypedDict):
    message_header: MessageHeader | MessageHeaderDict
    repeated_response_message_body: RepeatedResponseMessageBody | RepeatedResponseMessageBodyDict
