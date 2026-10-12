from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_detail_balance import AccountDetailBalance, AccountDetailBalanceDict
from .detail_balance1 import DetailBalance1, DetailBalance1Dict
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict


class AccountHolderBalanceResponse(SdkBaseModel):
    balance_per_account: Optional[list[AccountDetailBalance]] = Field(default=UNSET, alias="balancePerAccount")
    """A list of each account and their balances."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""

    total_balance: Optional[DetailBalance1] = Field(default=UNSET, alias="totalBalance")
    """The total balance of the account holder."""


class AccountHolderBalanceResponseDict(TypedDict):
    balance_per_account: NotRequired[list[AccountDetailBalanceDict]]
    invalid_fields: NotRequired[list[ErrorFieldTypeDict]]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
    total_balance: NotRequired[DetailBalance1Dict]
