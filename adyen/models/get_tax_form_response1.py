from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.content_type import ContentTypeOrStr


class GetTaxFormResponse1(SdkBaseModel):
    content: str
    """The content of the tax form in Base64 format."""

    content_type: Optional[ContentTypeOrStr] = Field(default=UNSET, alias="contentType")
    """The content type of the tax form.

    Possible values:
    * **application/pdf**"""


class GetTaxFormResponse1Dict(TypedDict):
    content: str
    content_type: NotRequired[ContentTypeOrStr]
