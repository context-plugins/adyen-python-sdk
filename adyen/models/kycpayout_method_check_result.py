from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .kyccheck_status_data import KyccheckStatusData, KyccheckStatusDataDict


class KycpayoutMethodCheckResult(SdkBaseModel):
    checks: Optional[list[KyccheckStatusData]] = UNSET
    """A list of the checks and their statuses."""

    payout_method_code: Optional[str] = Field(default=UNSET, alias="payoutMethodCode")
    """The unique ID of the payoput method to which the check applies."""


class KycpayoutMethodCheckResultDict(TypedDict):
    checks: NotRequired[list[KyccheckStatusData | KyccheckStatusDataDict]]
    payout_method_code: NotRequired[str]
