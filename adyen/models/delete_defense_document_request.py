from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeleteDefenseDocumentRequest(SdkBaseModel):
    defense_document_type: str = Field(alias="defenseDocumentType")
    """The document type code of the defense document."""

    dispute_psp_reference: str = Field(alias="disputePspReference")
    """The PSP reference assigned to the dispute."""

    merchant_account_code: str = Field(alias="merchantAccountCode")
    """The merchant account identifier, for which you want to process the dispute transaction."""


class DeleteDefenseDocumentRequestDict(TypedDict):
    defense_document_type: str
    dispute_psp_reference: str
    merchant_account_code: str
