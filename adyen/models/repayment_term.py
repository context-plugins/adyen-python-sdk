from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RepaymentTerm(SdkBaseModel):
    """An object containing the details of the configuration for repayment term., Contains information about the time
    period in which your user must repay the total amount of the grant."""

    estimated_days: int = Field(alias="estimatedDays")
    """The estimated term for repaying the grant, in days."""

    maximum_days: Optional[int] = Field(default=UNSET, alias="maximumDays")
    """The maximum term for repaying the grant, in days. Only applies when ``contractType`` is **loan**."""


class RepaymentTermDict(TypedDict):
    estimated_days: int
    maximum_days: NotRequired[int]
