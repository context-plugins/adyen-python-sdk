from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AcceptTermsOfServiceRequest(SdkBaseModel):
    accepted_by: str = Field(alias="acceptedBy")
    """The legal entity ID of the user accepting the Terms of Service.

    For organizations, this must be the individual legal entity ID of an authorized signatory for the organization.

    For sole proprietorships, this must be the individual legal entity ID of the owner.

    For individuals, this must be the individual legal entity id of either the individual, parent, or guardian."""

    ip_address: Optional[str] = Field(default=UNSET, alias="ipAddress")
    """The IP address of the user accepting the Terms of Service."""


class AcceptTermsOfServiceRequestDict(TypedDict):
    accepted_by: str
    ip_address: NotRequired[str]
