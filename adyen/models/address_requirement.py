from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.required_address_field import RequiredAddressFieldOrStr


class AddressRequirement(SdkBaseModel):
    description: Optional[str] = UNSET
    """Specifies the required address related fields for a particular route."""

    required_address_fields: Optional[list[RequiredAddressFieldOrStr]] = Field(
        default=UNSET, alias="requiredAddressFields"
    )
    """List of address fields."""

    type_: Literal["addressRequirement"] = Field(default="addressRequirement", alias="type")
    """**addressRequirement**"""


class AddressRequirementDict(TypedDict):
    description: NotRequired[str]
    required_address_fields: NotRequired[list[RequiredAddressFieldOrStr]]
    type_: Literal["addressRequirement"]
