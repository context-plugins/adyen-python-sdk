from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.attachment_type1 import AttachmentType1OrStr


class DisputeAttachment(SdkBaseModel):
    attachment_type: AttachmentType1OrStr = Field(alias="attachmentType")
    """The type of information contained in the attachment: **receipt**, **correspondence**, **other**."""

    content: str
    """The content of the image. An attachment must be base64-encoded data. Make sure that all base64-encoded data
    strings are generated without line breaks or "wrapping". For example, do not use ``Base64.NO_WRAP`` in Java, or its
    equivalent in other languages. Newline characters at the end of the base64-encoded data string will also result in a
    malformed input error."""

    file_name: str = Field(alias="fileName")
    """The name of the attachment, including its filename extension. Supported filename extensions: **jpeg**, **pdf**,
    **tiff**."""

    id: Optional[str] = UNSET
    """The unique identifier of the attachment."""


class DisputeAttachmentDict(TypedDict):
    attachment_type: AttachmentType1OrStr
    content: str
    file_name: str
    id: NotRequired[str]
