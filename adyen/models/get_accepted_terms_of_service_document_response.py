from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.terms_of_service_document_format import TermsOfServiceDocumentFormatOrStr


class GetAcceptedTermsOfServiceDocumentResponse(SdkBaseModel):
    document: Optional[str] = UNSET
    """The accepted Terms of Service document in the requested format represented as a Base64-encoded bytes array."""

    id: Optional[str] = UNSET
    """The unique identifier of the legal entity."""

    terms_of_service_acceptance_reference: Optional[str] = Field(
        default=UNSET, alias="termsOfServiceAcceptanceReference"
    )
    """An Adyen-generated reference for the accepted Terms of Service."""

    terms_of_service_document_format: Optional[TermsOfServiceDocumentFormatOrStr] = Field(
        default=UNSET, alias="termsOfServiceDocumentFormat"
    )
    """The format of the Terms of Service document."""


class GetAcceptedTermsOfServiceDocumentResponseDict(TypedDict):
    document: NotRequired[str]
    id: NotRequired[str]
    terms_of_service_acceptance_reference: NotRequired[str]
    terms_of_service_document_format: NotRequired[TermsOfServiceDocumentFormatOrStr]
