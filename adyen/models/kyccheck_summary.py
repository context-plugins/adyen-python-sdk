from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class KyccheckSummary(SdkBaseModel):
    kyc_check_code: Optional[int] = Field(default=UNSET, alias="kycCheckCode")
    """The code of the check. For possible values, refer to `Verification codes
    <https://docs.adyen.com/classic-platforms/verification-process/verification-codes>`__."""

    kyc_check_description: Optional[str] = Field(default=UNSET, alias="kycCheckDescription")
    """A description of the check."""


class KyccheckSummaryDict(TypedDict):
    kyc_check_code: NotRequired[int]
    kyc_check_description: NotRequired[str]
