from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .defense_document_type import DefenseDocumentType, DefenseDocumentTypeDict


class DefenseReason(SdkBaseModel):
    defense_document_types: Optional[list[DefenseDocumentType]] = Field(default=UNSET, alias="defenseDocumentTypes")
    """Array of defense document types for a specific defense reason. Indicates the document types that you can submit
    to the schemes to defend this dispute, and whether they are required."""

    defense_reason_code: str = Field(alias="defenseReasonCode")
    """The defense reason code that was selected to defend this dispute."""

    satisfied: bool
    """Indicates if sufficient defense material has been supplied."""


class DefenseReasonDict(TypedDict):
    defense_document_types: NotRequired[list[DefenseDocumentType | DefenseDocumentTypeDict]]
    defense_reason_code: str
    satisfied: bool
