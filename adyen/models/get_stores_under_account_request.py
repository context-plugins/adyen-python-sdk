from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetStoresUnderAccountRequest(SdkBaseModel):
    company_account: str = Field(alias="companyAccount")
    """The company account. If you only specify this parameter, the response includes the stores of all merchant
    accounts that are associated with the company account."""

    merchant_account: Optional[str] = Field(default=UNSET, alias="merchantAccount")
    """The merchant account. With this parameter, the response only includes the stores of the specified merchant
    account."""


class GetStoresUnderAccountRequestDict(TypedDict):
    company_account: str
    merchant_account: NotRequired[str]
