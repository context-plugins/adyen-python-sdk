from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RiskData(SdkBaseModel):
    client_data: Optional[str] = Field(default=UNSET, alias="clientData")
    """Contains client-side data, like the device fingerprint, cookies, and specific browser settings."""

    custom_fields: Optional[dict[str, str]] = Field(default=UNSET, alias="customFields")
    """Any custom fields used as part of the input to configured risk rules."""

    fraud_offset: Optional[int] = Field(default=UNSET, alias="fraudOffset")
    """An integer value that is added to the normal fraud score. The value can be either positive or negative."""

    profile_reference: Optional[str] = Field(default=UNSET, alias="profileReference")
    """The risk profile to assign to this payment. When left empty, the merchant-level account's default risk profile
    will be applied."""


class RiskDataDict(TypedDict):
    client_data: NotRequired[str]
    custom_fields: NotRequired[dict[str, str]]
    fraud_offset: NotRequired[int]
    profile_reference: NotRequired[str]
