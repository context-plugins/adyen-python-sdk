from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .repayment_term import RepaymentTerm, RepaymentTermDict
from .threshold_repayment21 import ThresholdRepayment21, ThresholdRepayment21Dict


class Repayment1(SdkBaseModel):
    basis_points: int = Field(alias="basisPoints")
    """The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage
    expressed in `basis points <https://www.investopedia.com/terms/b/basispoint.asp>`__."""

    term: Optional[RepaymentTerm] = UNSET
    """Contains information about the time period in which your user must repay the total amount of the grant."""

    threshold: Optional[ThresholdRepayment21] = UNSET
    """Contains the minimum threshold amount that your user must repay every 30-day period."""


class Repayment1Dict(TypedDict):
    basis_points: int
    term: NotRequired[RepaymentTermDict]
    threshold: NotRequired[ThresholdRepayment21Dict]
