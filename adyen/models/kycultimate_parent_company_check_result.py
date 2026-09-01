from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .kyccheck_status_data import KyccheckStatusData, KyccheckStatusDataDict


class KycultimateParentCompanyCheckResult(SdkBaseModel):
    checks: Optional[list[KyccheckStatusData]] = UNSET
    """A list of the checks and their statuses."""

    ultimate_parent_company_code: Optional[str] = Field(default=UNSET, alias="ultimateParentCompanyCode")
    """The code of the Ultimate Parent Company to which the check applies."""


class KycultimateParentCompanyCheckResultDict(TypedDict):
    checks: NotRequired[list[KyccheckStatusData | KyccheckStatusDataDict]]
    ultimate_parent_company_code: NotRequired[str]
