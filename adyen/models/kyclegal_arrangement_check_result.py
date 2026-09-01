from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .kyccheck_status_data import KyccheckStatusData, KyccheckStatusDataDict


class KyclegalArrangementCheckResult(SdkBaseModel):
    checks: Optional[list[KyccheckStatusData]] = UNSET
    """A list of the checks and their statuses."""

    legal_arrangement_code: Optional[str] = Field(default=UNSET, alias="legalArrangementCode")
    """The unique ID of the legal arrangement to which the check applies."""


class KyclegalArrangementCheckResultDict(TypedDict):
    checks: NotRequired[list[KyccheckStatusData | KyccheckStatusDataDict]]
    legal_arrangement_code: NotRequired[str]
