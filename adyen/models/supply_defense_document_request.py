from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .defense_document import DefenseDocument, DefenseDocumentDict


class SupplyDefenseDocumentRequest(SdkBaseModel):
    defense_documents: list[DefenseDocument] = Field(alias="defenseDocuments")
    """An array containing a list of the defense documents."""

    dispute_psp_reference: str = Field(alias="disputePspReference")
    """The PSP reference assigned to the dispute."""

    merchant_account_code: str = Field(alias="merchantAccountCode")
    """The merchant account identifier, for which you want to process the dispute transaction."""


class SupplyDefenseDocumentRequestDict(TypedDict):
    defense_documents: list[DefenseDocument | DefenseDocumentDict]
    dispute_psp_reference: str
    merchant_account_code: str
