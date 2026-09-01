from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .menu_entry import MenuEntry, MenuEntryDict
from .message_reference import MessageReference, MessageReferenceDict
from .output_content import OutputContent, OutputContentDict


class InputUpdate2(SdkBaseModel):
    """Content of the Input Update message."""

    message_reference: MessageReference = Field(alias="MessageReference")
    """Identification of a previous POI transaction. To abort a transaction in progress or to request the status of a
    transaction from which no response has been received. It identifies the message header of the message request to
    abort or request the status."""

    output_content: OutputContent = Field(alias="OutputContent")
    """Content to display or print. This is a sequence of elements if they have different formats."""

    menu_entry: Optional[list[MenuEntry]] = Field(default=UNSET, alias="MenuEntry")
    output_signature: Optional[str] = Field(default=UNSET, alias="OutputSignature")
    min_length: Optional[int] = Field(default=UNSET, alias="MinLength")
    max_length: Optional[int] = Field(default=UNSET, alias="MaxLength")
    max_decimal_length: Optional[int] = Field(default=UNSET, alias="MaxDecimalLength")


class InputUpdate2Dict(TypedDict):
    message_reference: MessageReference | MessageReferenceDict
    output_content: OutputContent | OutputContentDict
    menu_entry: NotRequired[list[MenuEntry | MenuEntryDict]]
    output_signature: NotRequired[str]
    min_length: NotRequired[int]
    max_length: NotRequired[int]
    max_decimal_length: NotRequired[int]
