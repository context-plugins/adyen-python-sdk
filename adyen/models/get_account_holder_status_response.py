from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_holder_status4 import AccountHolderStatus4, AccountHolderStatus4Dict
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict


class GetAccountHolderStatusResponse(SdkBaseModel):
    account_holder_code: Optional[str] = Field(default=UNSET, alias="accountHolderCode")
    """The code of the Account Holder."""

    account_holder_status: Optional[AccountHolderStatus4] = Field(default=UNSET, alias="accountHolderStatus")
    """The status of the Account Holder."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class GetAccountHolderStatusResponseDict(TypedDict):
    account_holder_code: NotRequired[str]
    account_holder_status: NotRequired[AccountHolderStatus4Dict]
    invalid_fields: NotRequired[list[ErrorFieldTypeDict]]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
