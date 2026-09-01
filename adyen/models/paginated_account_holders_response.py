from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_holder import AccountHolder, AccountHolderDict


class PaginatedAccountHoldersResponse(SdkBaseModel):
    account_holders: list[AccountHolder] = Field(alias="accountHolders")
    """List of account holders."""

    has_next: bool = Field(alias="hasNext")
    """Indicates whether there are more items on the next page."""

    has_previous: bool = Field(alias="hasPrevious")
    """Indicates whether there are more items on the previous page."""


class PaginatedAccountHoldersResponseDict(TypedDict):
    account_holders: list[AccountHolder | AccountHolderDict]
    has_next: bool
    has_previous: bool
