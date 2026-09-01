from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeleteSignatoriesRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the account holder from which to delete the signatories."""

    signatory_codes: list[str] = Field(alias="signatoryCodes")
    """Array of codes of the signatories to be deleted."""


class DeleteSignatoriesRequestDict(TypedDict):
    account_holder_code: str
    signatory_codes: list[str]
