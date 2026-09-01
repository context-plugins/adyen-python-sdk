from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payout_speed import PayoutSpeedOrStr
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict


class PayoutAccountHolderResponse(SdkBaseModel):
    bank_account_uuid: Optional[str] = Field(default=UNSET, alias="bankAccountUUID")
    """The unique ID of the Bank Account to which the payout was made."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """The value supplied by the executing user when initiating the transfer; may be used to link multiple
    transactions."""

    payout_speed: Optional[PayoutSpeedOrStr] = Field(default=UNSET, alias="payoutSpeed")
    """Speed with which payouts for this account are processed. Permitted values: ``STANDARD``, ``SAME_DAY``."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class PayoutAccountHolderResponseDict(TypedDict):
    bank_account_uuid: NotRequired[str]
    invalid_fields: NotRequired[list[ErrorFieldType | ErrorFieldTypeDict]]
    merchant_reference: NotRequired[str]
    payout_speed: NotRequired[PayoutSpeedOrStr]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
