from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FindTerminalResponse(SdkBaseModel):
    company_account: str = Field(alias="companyAccount")
    """The company account that the terminal is associated with. If this is the only account level shown in the
    response, the terminal is assigned to the inventory of the company account."""

    merchant_account: Optional[str] = Field(default=UNSET, alias="merchantAccount")
    """The merchant account that the terminal is associated with. If the response doesn't contain a ``store`` the
    terminal is assigned to this merchant account."""

    merchant_inventory: Optional[bool] = Field(default=UNSET, alias="merchantInventory")
    """Boolean that indicates if the terminal is assigned to the merchant inventory. This is returned when the terminal
    is assigned to a merchant account.

    - If **true**, this indicates that the terminal is in the merchant inventory. This also means that the terminal
        cannot be boarded.

    - If **false**, this indicates that the terminal is assigned to the merchant account as an in-store terminal. This
        means that the terminal is ready to be boarded, or is already boarded."""

    store: Optional[str] = UNSET
    """The store code of the store that the terminal is assigned to."""

    terminal: str
    """The unique terminal ID."""


class FindTerminalResponseDict(TypedDict):
    company_account: str
    merchant_account: NotRequired[str]
    merchant_inventory: NotRequired[bool]
    store: NotRequired[str]
    terminal: str
