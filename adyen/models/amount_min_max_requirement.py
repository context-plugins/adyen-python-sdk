from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AmountMinMaxRequirement(SdkBaseModel):
    description: Optional[str] = UNSET
    """Specifies the eligible amounts for a particular route."""

    max: Optional[int] = UNSET
    """Maximum amount."""

    min: Optional[int] = UNSET
    """Minimum amount."""

    type_: Literal["amountMinMaxRequirement"] = Field(default="amountMinMaxRequirement", alias="type")
    """**amountMinMaxRequirement**"""


class AmountMinMaxRequirementDict(TypedDict):
    description: NotRequired[str]
    max: NotRequired[int]
    min: NotRequired[int]
    type_: NotRequired[Literal["amountMinMaxRequirement"]]
