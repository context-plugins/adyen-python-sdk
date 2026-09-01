from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EftaccountIdentifier(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The account number of the bank account."""

    branch: str
    """Identifies the specific branch where the account is held within the Canadian banking system."""

    institution: str
    """The financial institution that identifies the bank in Canada."""


class EftaccountIdentifierDict(TypedDict):
    account_number: str
    branch: str
    institution: str
