from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeleteShareholderRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the Account Holder from which to delete the Shareholders."""

    shareholder_codes: list[str] = Field(alias="shareholderCodes")
    """The code(s) of the Shareholders to be deleted."""


class DeleteShareholderRequestDict(TypedDict):
    account_holder_code: str
    shareholder_codes: list[str]
