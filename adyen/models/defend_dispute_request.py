from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DefendDisputeRequest(SdkBaseModel):
    defense_reason_code: str = Field(alias="defenseReasonCode")
    """The defense reason code that was selected to defend this dispute."""

    dispute_psp_reference: str = Field(alias="disputePspReference")
    """The PSP reference assigned to the dispute."""

    merchant_account_code: str = Field(alias="merchantAccountCode")
    """The merchant account identifier, for which you want to process the dispute transaction."""


class DefendDisputeRequestDict(TypedDict):
    defense_reason_code: str
    dispute_psp_reference: str
    merchant_account_code: str
