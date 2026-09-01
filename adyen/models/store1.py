from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address14 import Address14, Address14Dict


class Store1(SdkBaseModel):
    address: Optional[Address14] = UNSET
    """The address of the store."""

    description: Optional[str] = UNSET
    """The description of the store."""

    in_store_terminals: Optional[list[str]] = Field(default=UNSET, alias="inStoreTerminals")
    """The list of terminals assigned to the store."""

    merchant_account_code: Optional[str] = Field(default=UNSET, alias="merchantAccountCode")
    """The code of the merchant account."""

    status: Optional[str] = UNSET
    """The status of the store:

    - ``PreActive``: the store has been created, but not yet activated.

    - ``Active``: the store has been activated. This means you can process payments for this store.

    - ``Inactive``: the store is currently not active.

    - ``InactiveWithModifications``: the store is currently not active, but payment modifications such as refunds are
        possible.

    - ``Closed``: the store has been closed."""

    store: str
    """The code of the store."""


class Store1Dict(TypedDict):
    address: NotRequired[Address14 | Address14Dict]
    description: NotRequired[str]
    in_store_terminals: NotRequired[list[str]]
    merchant_account_code: NotRequired[str]
    status: NotRequired[str]
    store: str
