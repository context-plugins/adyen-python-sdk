from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict


class DebitAccountHolderResponse(SdkBaseModel):
    account_holder_code: Optional[str] = Field(default=UNSET, alias="accountHolderCode")
    """The code of the account holder."""

    bank_account_uuid: Optional[str] = Field(default=UNSET, alias="bankAccountUUID")
    """The Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    merchant_references: Optional[list[str]] = Field(default=UNSET, alias="merchantReferences")
    """List of the ``reference`` values from the ``split`` array in the request."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class DebitAccountHolderResponseDict(TypedDict):
    account_holder_code: NotRequired[str]
    bank_account_uuid: NotRequired[str]
    invalid_fields: NotRequired[list[ErrorFieldTypeDict]]
    merchant_references: NotRequired[list[str]]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
