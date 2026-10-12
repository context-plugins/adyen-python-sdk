from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict


class RefundFundsTransferResponse(SdkBaseModel):
    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """The value supplied by the executing user when initiating the transfer refund; may be used to link multiple
    transactions."""

    message: Optional[str] = UNSET
    """The message of the response."""

    original_reference: Optional[str] = Field(default=UNSET, alias="originalReference")
    """A PSP reference of the original fund transfer."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class RefundFundsTransferResponseDict(TypedDict):
    invalid_fields: NotRequired[list[ErrorFieldTypeDict]]
    merchant_reference: NotRequired[str]
    message: NotRequired[str]
    original_reference: NotRequired[str]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
