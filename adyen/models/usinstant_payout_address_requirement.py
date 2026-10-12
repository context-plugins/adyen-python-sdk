from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsinstantPayoutAddressRequirement(SdkBaseModel):
    description: Optional[str] = UNSET
    """Specifies that you must provide complete street addresses for the party and counterParty for transactions greater
    than USD 3000."""

    type_: Literal["usInstantPayoutAddressRequirement"] = Field(
        default="usInstantPayoutAddressRequirement", alias="type"
    )
    """**usInstantPayoutAddressRequirement**"""


class UsinstantPayoutAddressRequirementDict(TypedDict):
    description: NotRequired[str]
    type_: Literal["usInstantPayoutAddressRequirement"]
