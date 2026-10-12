from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .kyccheck_status_data import KyccheckStatusData, KyccheckStatusDataDict


class KyccheckResult(SdkBaseModel):
    checks: Optional[list[KyccheckStatusData]] = UNSET
    """A list of the checks and their statuses."""


class KyccheckResultDict(TypedDict):
    checks: NotRequired[list[KyccheckStatusDataDict]]
