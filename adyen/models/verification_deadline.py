from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.capability import CapabilityOrStr


class VerificationDeadline(SdkBaseModel):
    capabilities: list[CapabilityOrStr]
    """The names of the capabilities to be disallowed."""

    entity_ids: Optional[list[str]] = Field(default=UNSET, alias="entityIds")
    """The unique identifiers of the bank account(s) that the deadline applies to"""

    expires_at: RFC3339DateTime = Field(alias="expiresAt")
    """The date that verification is due by before capabilities are disallowed."""


class VerificationDeadlineDict(TypedDict):
    capabilities: list[CapabilityOrStr]
    entity_ids: NotRequired[list[str]]
    expires_at: RFC3339DateTime
