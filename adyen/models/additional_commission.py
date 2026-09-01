from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalCommission(SdkBaseModel):
    balance_account_id: Optional[str] = Field(default=UNSET, alias="balanceAccountId")
    """Unique identifier of the balance account to which the additional commission is booked."""

    fixed_amount: Optional[int] = Field(default=UNSET, alias="fixedAmount")
    """A fixed commission fee, in minor units."""

    variable_percentage: Optional[int] = Field(default=UNSET, alias="variablePercentage")
    """A variable commission fee, in basis points."""


class AdditionalCommissionDict(TypedDict):
    balance_account_id: NotRequired[str]
    fixed_amount: NotRequired[int]
    variable_percentage: NotRequired[int]
