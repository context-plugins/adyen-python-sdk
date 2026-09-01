from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UnSuspendAccountHolderRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the account holder to be reinstated."""


class UnSuspendAccountHolderRequestDict(TypedDict):
    account_holder_code: str
