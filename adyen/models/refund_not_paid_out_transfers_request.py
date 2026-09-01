from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RefundNotPaidOutTransfersRequest(SdkBaseModel):
    account_code: str = Field(alias="accountCode")
    """The code of the account from which to perform the refund(s)."""

    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the Account Holder which owns the account from which to perform the refund(s)."""


class RefundNotPaidOutTransfersRequestDict(TypedDict):
    account_code: str
    account_holder_code: str
