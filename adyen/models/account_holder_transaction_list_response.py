from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_transaction_list import AccountTransactionList, AccountTransactionListDict
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict


class AccountHolderTransactionListResponse(SdkBaseModel):
    account_transaction_lists: Optional[list[AccountTransactionList]] = Field(
        default=UNSET, alias="accountTransactionLists"
    )
    """A list of the transactions."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class AccountHolderTransactionListResponseDict(TypedDict):
    account_transaction_lists: NotRequired[list[AccountTransactionList | AccountTransactionListDict]]
    invalid_fields: NotRequired[list[ErrorFieldType | ErrorFieldTypeDict]]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
