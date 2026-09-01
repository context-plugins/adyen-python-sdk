from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.account_state_type import AccountStateTypeOrStr


class PerformVerificationRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the account holder to verify."""

    account_state_type: AccountStateTypeOrStr = Field(alias="accountStateType")
    """The state required for the account holder.
    > Permitted values: ``Processing``, ``Payout``."""

    tier: int
    """The tier required for the account holder."""


class PerformVerificationRequestDict(TypedDict):
    account_holder_code: str
    account_state_type: AccountStateTypeOrStr
    tier: int
