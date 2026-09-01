from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .repayment_term import RepaymentTerm, RepaymentTermDict
from .threshold_repayment2 import ThresholdRepayment2, ThresholdRepayment2Dict


class Repayment(SdkBaseModel):
    """An object containing the details of the 30-day repayment threshold."""

    basis_points: int = Field(alias="basisPoints")
    """The repayment that is deducted daily from incoming net volume, in `basis points
    <https://www.investopedia.com/terms/b/basispoint.asp>`__."""

    term: Optional[RepaymentTerm] = UNSET
    """An object containing the details of the configuration for repayment term."""

    threshold: Optional[ThresholdRepayment2] = UNSET
    """An object containing the details of the 30-day repayment threshold."""


class RepaymentDict(TypedDict):
    basis_points: int
    term: NotRequired[RepaymentTerm | RepaymentTermDict]
    threshold: NotRequired[ThresholdRepayment2 | ThresholdRepayment2Dict]
