from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .merchant_account import MerchantAccount, MerchantAccountDict


class GetTerminalsUnderAccountResponse(SdkBaseModel):
    company_account: str = Field(alias="companyAccount")
    """Your company account."""

    inventory_terminals: Optional[list[str]] = Field(default=UNSET, alias="inventoryTerminals")
    """Array that returns a list of all terminals that are in the inventory of the company account."""

    merchant_accounts: Optional[list[MerchantAccount]] = Field(default=UNSET, alias="merchantAccounts")
    """Array that returns a list of all merchant accounts belonging to the company account."""


class GetTerminalsUnderAccountResponseDict(TypedDict):
    company_account: str
    inventory_terminals: NotRequired[list[str]]
    merchant_accounts: NotRequired[list[MerchantAccount | MerchantAccountDict]]
