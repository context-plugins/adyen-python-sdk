from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .kyccheck_status_data import KyccheckStatusData, KyccheckStatusDataDict


class KycsignatoryCheckResult(SdkBaseModel):
    checks: Optional[list[KyccheckStatusData]] = UNSET
    """A list of the checks and their statuses."""

    signatory_code: Optional[str] = Field(default=UNSET, alias="signatoryCode")
    """The code of the signatory to which the check applies."""


class KycsignatoryCheckResultDict(TypedDict):
    checks: NotRequired[list[KyccheckStatusData | KyccheckStatusDataDict]]
    signatory_code: NotRequired[str]
