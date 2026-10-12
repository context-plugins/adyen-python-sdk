from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .kyccheck_status_data import KyccheckStatusData, KyccheckStatusDataDict


class KyccheckResult2(SdkBaseModel):
    """The results of the checks on the account holder."""

    checks: Optional[list[KyccheckStatusData]] = UNSET
    """A list of the checks and their statuses."""


class KyccheckResult2Dict(TypedDict):
    checks: NotRequired[list[KyccheckStatusDataDict]]
