from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PhoneInfo2(SdkBaseModel):
    """The information about the phone number of the device used to provision the the network token. This object is
    conditionally returned and is available for up to 24 hours after the provisioning request (access to this field
    requires a specific user role, please contact your Adyen representative to request permission)."""

    hashed_number: Optional[str] = Field(default=UNSET, alias="hashedNumber")
    """The hashed value of the phone number used to provision the network token."""

    last_four_digits: Optional[str] = Field(default=UNSET, alias="lastFourDigits")
    """The last four digits of the phone number used to provision the network token."""

    number: Optional[str] = UNSET
    """The full phone number of the device used to provision the network token."""


class PhoneInfo2Dict(TypedDict):
    hashed_number: NotRequired[str]
    last_four_digits: NotRequired[str]
    number: NotRequired[str]
