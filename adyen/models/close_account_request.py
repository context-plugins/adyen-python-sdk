from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CloseAccountRequest(SdkBaseModel):
    account_code: str = Field(alias="accountCode")
    """The code of account to be closed."""


class CloseAccountRequestDict(TypedDict):
    account_code: str
