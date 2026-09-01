from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DefenseDocument(SdkBaseModel):
    content: str
    """The content of the defense document."""

    content_type: str = Field(alias="contentType")
    """The content type of the defense document."""

    defense_document_type_code: str = Field(alias="defenseDocumentTypeCode")
    """The document type code of the defense document."""


class DefenseDocumentDict(TypedDict):
    content: str
    content_type: str
    defense_document_type_code: str
