from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .repayment_term import RepaymentTerm, RepaymentTermDict


class DynamicOfferRepayment(SdkBaseModel):
    term: RepaymentTerm
    """Contains information about the time period in which your user must repay the total amount of the grant."""


class DynamicOfferRepaymentDict(TypedDict):
    term: RepaymentTerm | RepaymentTermDict
