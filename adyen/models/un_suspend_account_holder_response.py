from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_holder_status1 import AccountHolderStatus1, AccountHolderStatus1Dict
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict


class UnSuspendAccountHolderResponse(SdkBaseModel):
    account_holder_status: Optional[AccountHolderStatus1] = Field(default=UNSET, alias="accountHolderStatus")
    """The new status of the Account Holder."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class UnSuspendAccountHolderResponseDict(TypedDict):
    account_holder_status: NotRequired[AccountHolderStatus1Dict]
    invalid_fields: NotRequired[list[ErrorFieldTypeDict]]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
