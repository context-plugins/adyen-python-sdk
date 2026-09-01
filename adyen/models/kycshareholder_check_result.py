from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .kyccheck_status_data import KyccheckStatusData, KyccheckStatusDataDict


class KycshareholderCheckResult(SdkBaseModel):
    checks: Optional[list[KyccheckStatusData]] = UNSET
    """A list of the checks and their statuses."""

    legal_arrangement_code: Optional[str] = Field(default=UNSET, alias="legalArrangementCode")
    """The unique ID of the legal arrangement to which the shareholder belongs, if applicable."""

    legal_arrangement_entity_code: Optional[str] = Field(default=UNSET, alias="legalArrangementEntityCode")
    """The unique ID of the legal arrangement entity to which the shareholder belongs, if applicable."""

    shareholder_code: Optional[str] = Field(default=UNSET, alias="shareholderCode")
    """The code of the shareholder to which the check applies."""


class KycshareholderCheckResultDict(TypedDict):
    checks: NotRequired[list[KyccheckStatusData | KyccheckStatusDataDict]]
    legal_arrangement_code: NotRequired[str]
    legal_arrangement_entity_code: NotRequired[str]
    shareholder_code: NotRequired[str]
