from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type64 import Type64OrStr


class GetTermsOfServiceDocumentRequest(SdkBaseModel):
    language: str
    """The language to be used for the Terms of Service document, specified by the two-letter `ISO 639-1
    <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`__ language code. Possible values: **en** for English or
    **fr** for French."""

    terms_of_service_document_format: Optional[str] = Field(default=UNSET, alias="termsOfServiceDocumentFormat")
    """The requested format for the Terms of Service document. Default value: JSON. Possible values: **JSON**, **PDF**,
    or **TXT**."""

    type_: Type64OrStr = Field(alias="type")
    """The type of Terms of Service.

    Possible values:
    * **adyenForPlatformsManage**
    * **adyenIssuing**
    * **adyenForPlatformsAdvanced**
    * **adyenCapital**
    * **adyenAccount**
    * **adyenCard**
    * **adyenFranchisee**
    * **adyenPccr**
    * **adyenChargeCard**
    * **kycOnInvite**"""


class GetTermsOfServiceDocumentRequestDict(TypedDict):
    language: str
    terms_of_service_document_format: NotRequired[str]
    type_: Type64OrStr
