from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsinternationalAchAddressRequirement(SdkBaseModel):
    description: Optional[str] = UNSET
    """Specifies that you must provide a complete street address for International ACH (IAT) transactions."""

    type_: Literal["usInternationalAchAddressRequirement"] = Field(
        default="usInternationalAchAddressRequirement", alias="type"
    )
    """**usInternationalAchAddressRequirement**"""


class UsinternationalAchAddressRequirementDict(TypedDict):
    description: NotRequired[str]
    type_: Literal["usInternationalAchAddressRequirement"]
