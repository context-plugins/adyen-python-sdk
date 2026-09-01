from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .document_page import DocumentPage, DocumentPageDict


class DocumentReference(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Identifies whether the document is active and used for checks."""

    description: Optional[str] = UNSET
    """Your description for the document."""

    file_name: Optional[str] = Field(default=UNSET, alias="fileName")
    """Document name."""

    id: Optional[str] = UNSET
    """The unique identifier of the resource."""

    modification_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="modificationDate")
    """The modification date of the document."""

    pages: Optional[list[DocumentPage]] = UNSET
    """List of document pages"""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Type of document, used when providing an ID number or uploading a document."""


class DocumentReferenceDict(TypedDict):
    active: NotRequired[bool]
    description: NotRequired[str]
    file_name: NotRequired[str]
    id: NotRequired[str]
    modification_date: NotRequired[RFC3339DateTime]
    pages: NotRequired[list[DocumentPage | DocumentPageDict]]
    type_: NotRequired[str]
