from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsinternationalAchPriorityRequirement(SdkBaseModel):
    description: Optional[str] = UNSET
    """Specifies that transactions deemed to be International ACH (IAT) per OFAC/NACHA rules cannot have fast
    priority."""

    type_: Literal["usInternationalAchPriorityRequirement"] = Field(
        default="usInternationalAchPriorityRequirement", alias="type"
    )
    """**usInternationalAchPriorityRequirement**"""


class UsinternationalAchPriorityRequirementDict(TypedDict):
    description: NotRequired[str]
    type_: NotRequired[Literal["usInternationalAchPriorityRequirement"]]
