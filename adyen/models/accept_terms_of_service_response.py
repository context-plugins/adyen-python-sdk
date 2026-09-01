from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type64 import Type64OrStr


class AcceptTermsOfServiceResponse(SdkBaseModel):
    accepted_by: Optional[str] = Field(default=UNSET, alias="acceptedBy")
    """The unique identifier of the user that accepted the Terms of Service."""

    id: Optional[str] = UNSET
    """The unique identifier of the Terms of Service acceptance."""

    ip_address: Optional[str] = Field(default=UNSET, alias="ipAddress")
    """The IP address of the user that accepted the Terms of Service."""

    language: Optional[str] = UNSET
    """The language used for the Terms of Service document, specified by the two-letter `ISO 639-1
    <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`__ language code. Possible value: **en** for English or
    **fr** for French.

    Note that French is only available for some integration types in certain countries/regions. Reach out to your Adyen
    contact for more information."""

    terms_of_service_document_id: Optional[str] = Field(default=UNSET, alias="termsOfServiceDocumentId")
    """The unique identifier of the Terms of Service document."""

    type_: Optional[Type64OrStr] = Field(default=UNSET, alias="type")
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


class AcceptTermsOfServiceResponseDict(TypedDict):
    accepted_by: NotRequired[str]
    id: NotRequired[str]
    ip_address: NotRequired[str]
    language: NotRequired[str]
    terms_of_service_document_id: NotRequired[str]
    type_: NotRequired[Type64OrStr]
