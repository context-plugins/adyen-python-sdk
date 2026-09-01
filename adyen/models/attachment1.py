from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Attachment1(SdkBaseModel):
    """Object that contains the document."""

    content: str
    """The document in Base64-encoded string format."""

    content_type: Optional[str] = Field(default=UNSET, alias="contentType")
    """The file format.

     Possible values: **application/pdf**, **image/jpg**, **image/jpeg**, **image/png**."""

    filename: Optional[str] = UNSET
    """The name of the file including the file extension."""

    page_name: Optional[str] = Field(default=UNSET, alias="pageName")
    """The name of the file including the file extension."""

    page_type: Optional[str] = Field(default=UNSET, alias="pageType")
    """Specifies which side of the ID card is uploaded.

    * If the ``type`` is **driversLicense** or **identityCard**, you must set this to **front** or **back** and include
        both sides in the same API request.

    * For any other types, when this is omitted, we infer the page number based on the order of attachments."""


class Attachment1Dict(TypedDict):
    content: str
    content_type: NotRequired[str]
    filename: NotRequired[str]
    page_name: NotRequired[str]
    page_type: NotRequired[str]
