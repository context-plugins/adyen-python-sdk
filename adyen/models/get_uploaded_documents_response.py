from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .document_detail import DocumentDetail, DocumentDetailDict
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict


class GetUploadedDocumentsResponse(SdkBaseModel):
    document_details: Optional[list[DocumentDetail]] = Field(default=UNSET, alias="documentDetails")
    """A list of the documents and their details."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class GetUploadedDocumentsResponseDict(TypedDict):
    document_details: NotRequired[list[DocumentDetail | DocumentDetailDict]]
    invalid_fields: NotRequired[list[ErrorFieldType | ErrorFieldTypeDict]]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
