from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict


class GetTaxFormResponse(SdkBaseModel):
    content: Optional[str] = UNSET
    """The content of the tax form in the Base64 binary format."""

    content_type: Optional[str] = Field(default=UNSET, alias="contentType")
    """The content type of the tax form."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class GetTaxFormResponseDict(TypedDict):
    content: NotRequired[str]
    content_type: NotRequired[str]
    invalid_fields: NotRequired[list[ErrorFieldTypeDict]]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
