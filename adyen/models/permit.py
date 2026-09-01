from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .permit_restriction2 import PermitRestriction2, PermitRestriction2Dict


class Permit(SdkBaseModel):
    partner_id: Optional[str] = Field(default=UNSET, alias="partnerId")
    """Partner ID (when using the permit-per-partner token sharing model)."""

    profile_reference: Optional[str] = Field(default=UNSET, alias="profileReference")
    """The profile to apply to this permit (when using the shared permits model)."""

    restriction: Optional[PermitRestriction2] = UNSET
    """Permit level restriction overrides."""

    result_key: Optional[str] = Field(default=UNSET, alias="resultKey")
    """The key to link permit requests to permit results."""

    valid_till_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="validTillDate")
    """The expiry date for this permit."""


class PermitDict(TypedDict):
    partner_id: NotRequired[str]
    profile_reference: NotRequired[str]
    restriction: NotRequired[PermitRestriction2 | PermitRestriction2Dict]
    result_key: NotRequired[str]
    valid_till_date: NotRequired[RFC3339DateTime]
