from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AttachDocumentResponse(SdkBaseModel):
    attachment_id: Optional[str] = Field(default=UNSET, alias="attachmentId")
    """The unique identifier of the attachment."""


class AttachDocumentResponseDict(TypedDict):
    attachment_id: NotRequired[str]
