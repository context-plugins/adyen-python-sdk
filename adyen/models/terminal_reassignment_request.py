from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TerminalReassignmentRequest(SdkBaseModel):
    company_id: Optional[str] = Field(default=UNSET, alias="companyId")
    """The unique identifier of the company account to which the terminal is reassigned."""

    inventory: Optional[bool] = UNSET
    """Must be specified when reassigning terminals to a merchant account:

    - If set to **true**, reassigns terminals to the inventory of the merchant account and the terminals cannot process
        transactions.

    - If set to **false**, reassigns terminals directly to the merchant account and the terminals can process
        transactions."""

    merchant_id: Optional[str] = Field(default=UNSET, alias="merchantId")
    """The unique identifier of the merchant account to which the terminal is reassigned. When reassigning terminals to
    a merchant account, you must specify the ``inventory`` field."""

    store_id: Optional[str] = Field(default=UNSET, alias="storeId")
    """The unique identifier of the store to which the terminal is reassigned."""


class TerminalReassignmentRequestDict(TypedDict):
    company_id: NotRequired[str]
    inventory: NotRequired[bool]
    merchant_id: NotRequired[str]
    store_id: NotRequired[str]
