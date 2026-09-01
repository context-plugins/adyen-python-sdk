from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Commission1(SdkBaseModel):
    """Defines your platform's commission for the processed payments as a fixed amount (specified in minor units), a
    percentage (specified in basis points), or both. The commission is booked to your platform's liable balance
    account."""

    fixed_amount: Optional[int] = Field(default=UNSET, alias="fixedAmount")
    """A fixed commission fee, in minor units."""

    variable_percentage: Optional[int] = Field(default=UNSET, alias="variablePercentage")
    """A variable commission fee, in basis points."""


class Commission1Dict(TypedDict):
    fixed_amount: NotRequired[int]
    variable_percentage: NotRequired[int]
