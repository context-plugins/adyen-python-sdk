from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TerminalReassignmentTarget2(SdkBaseModel):
    """Indicates where the terminal is in the process of being reassigned to."""

    company_id: Optional[str] = Field(default=UNSET, alias="companyId")
    """The unique identifier of the company account to which the terminal is reassigned."""

    inventory: bool
    """Indicates if the terminal is reassigned to the inventory of the merchant account.
    - If **true**, the terminal is in the inventory of the merchant account and cannot process transactions.
    - If **false**, the terminal is reassigned directly to the merchant account and can process transactions."""

    merchant_id: Optional[str] = Field(default=UNSET, alias="merchantId")
    """The unique identifier of the merchant account to which the terminal is reassigned."""

    store_id: Optional[str] = Field(default=UNSET, alias="storeId")
    """The unique identifier of the store to which the terminal is reassigned."""


class TerminalReassignmentTarget2Dict(TypedDict):
    company_id: NotRequired[str]
    inventory: bool
    merchant_id: NotRequired[str]
    store_id: NotRequired[str]
