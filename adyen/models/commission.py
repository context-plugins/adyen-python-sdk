from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Commission(SdkBaseModel):
    fixed_amount: Optional[int] = Field(default=UNSET, alias="fixedAmount")
    """A fixed commission fee, in minor units."""

    variable_percentage: Optional[int] = Field(default=UNSET, alias="variablePercentage")
    """A variable commission fee, in basis points."""


class CommissionDict(TypedDict):
    fixed_amount: NotRequired[int]
    variable_percentage: NotRequired[int]
