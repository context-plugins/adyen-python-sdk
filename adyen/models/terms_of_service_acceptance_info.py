from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.type64 import Type64OrStr


class TermsOfServiceAcceptanceInfo(SdkBaseModel):
    accepted_by: Optional[str] = Field(default=UNSET, alias="acceptedBy")
    """The unique identifier of the user that accepted the Terms of Service."""

    accepted_for: Optional[str] = Field(default=UNSET, alias="acceptedFor")
    """The unique identifier of the legal entity for which the Terms of Service are accepted."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """The date when the Terms of Service were accepted, in ISO 8601 extended format. For example,
    2022-12-18T10:15:30+01:00."""

    id: Optional[str] = UNSET
    """An Adyen-generated reference for the accepted Terms of Service."""

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

    valid_to: Optional[RFC3339DateTime] = Field(default=UNSET, alias="validTo")
    """The expiration date for the Terms of Service acceptance, in ISO 8601 extended format. For example,
    2022-12-18T00:00:00+01:00."""


class TermsOfServiceAcceptanceInfoDict(TypedDict):
    accepted_by: NotRequired[str]
    accepted_for: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    id: NotRequired[str]
    type_: NotRequired[Type64OrStr]
    valid_to: NotRequired[RFC3339DateTime]
