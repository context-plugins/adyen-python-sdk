from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .document_detail1 import DocumentDetail1, DocumentDetail1Dict


class UploadDocumentRequest(SdkBaseModel):
    document_content: str = Field(alias="documentContent")
    """The content of the document, in Base64-encoded string format.

    To learn about document requirements, refer to `Verification checks
    <https://docs.adyen.com/classic-platforms/verification-checks>`__."""

    document_detail: DocumentDetail1 = Field(alias="documentDetail")
    """Details of the document being submitted."""


class UploadDocumentRequestDict(TypedDict):
    document_content: str
    document_detail: DocumentDetail1Dict
