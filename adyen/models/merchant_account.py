from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .store1 import Store1, Store1Dict


class MerchantAccount(SdkBaseModel):
    in_store_terminals: Optional[list[str]] = Field(default=UNSET, alias="inStoreTerminals")
    """List of terminals assigned to this merchant account as in-store terminals. This means that the terminal is ready
    to be boarded, or is already boarded."""

    inventory_terminals: Optional[list[str]] = Field(default=UNSET, alias="inventoryTerminals")
    """List of terminals assigned to the inventory of this merchant account."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account."""

    stores: Optional[list[Store1]] = UNSET
    """Array of stores under this merchant account."""


class MerchantAccountDict(TypedDict):
    in_store_terminals: NotRequired[list[str]]
    inventory_terminals: NotRequired[list[str]]
    merchant_account: str
    stores: NotRequired[list[Store1Dict]]
