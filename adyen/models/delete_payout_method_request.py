from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeletePayoutMethodRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the account holder, from which to delete the payout methods."""

    payout_method_codes: list[str] = Field(alias="payoutMethodCodes")
    """The codes of the payout methods to be deleted."""


class DeletePayoutMethodRequestDict(TypedDict):
    account_holder_code: str
    payout_method_codes: list[str]
