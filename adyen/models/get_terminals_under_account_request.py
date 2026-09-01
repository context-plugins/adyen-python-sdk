from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetTerminalsUnderAccountRequest(SdkBaseModel):
    company_account: str = Field(alias="companyAccount")
    """Your company account. If you only specify this parameter, the response includes all terminals at all account
    levels."""

    merchant_account: Optional[str] = Field(default=UNSET, alias="merchantAccount")
    """The merchant account. This is required if you are retrieving the terminals assigned to a store.If you don't
    specify a ``store`` the response includes the terminals assigned to the specified merchant account and the terminals
    assigned to the stores under this merchant account."""

    store: Optional[str] = UNSET
    """The store code of the store. With this parameter, the response only includes the terminals assigned to the
    specified store."""


class GetTerminalsUnderAccountRequestDict(TypedDict):
    company_account: str
    merchant_account: NotRequired[str]
    store: NotRequired[str]
