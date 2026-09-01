from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payout_speed import PayoutSpeedOrStr
from .enums.status42 import Status42OrStr
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict
from .payout_schedule_response1 import PayoutScheduleResponse1, PayoutScheduleResponse1Dict


class CreateAccountResponse(SdkBaseModel):
    account_code: Optional[str] = Field(default=UNSET, alias="accountCode")
    """The code of the new account."""

    account_holder_code: Optional[str] = Field(default=UNSET, alias="accountHolderCode")
    """The code of the account holder."""

    bank_account_uuid: Optional[str] = Field(default=UNSET, alias="bankAccountUUID")
    """The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts
    in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different
    currencies will be sent to a matching bank account of the account holder."""

    description: Optional[str] = UNSET
    """The description of the account."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """A list of fields that caused the ``/createAccount`` request to fail."""

    metadata: Optional[dict[str, str]] = UNSET
    """A set of key and value pairs containing metadata."""

    payout_method_code: Optional[str] = Field(default=UNSET, alias="payoutMethodCode")
    """The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent
    using this payout method code."""

    payout_schedule: Optional[PayoutScheduleResponse1] = Field(default=UNSET, alias="payoutSchedule")
    """The details of the payout schedule added to the account."""

    payout_speed: Optional[PayoutSpeedOrStr] = Field(default=UNSET, alias="payoutSpeed")
    """Speed with which payouts for this account are processed. Permitted values: ``STANDARD``, ``SAME_DAY``."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""

    status: Optional[Status42OrStr] = UNSET
    """The status of the account. >Permitted values: ``Active``."""


class CreateAccountResponseDict(TypedDict):
    account_code: NotRequired[str]
    account_holder_code: NotRequired[str]
    bank_account_uuid: NotRequired[str]
    description: NotRequired[str]
    invalid_fields: NotRequired[list[ErrorFieldType | ErrorFieldTypeDict]]
    metadata: NotRequired[dict[str, str]]
    payout_method_code: NotRequired[str]
    payout_schedule: NotRequired[PayoutScheduleResponse1 | PayoutScheduleResponse1Dict]
    payout_speed: NotRequired[PayoutSpeedOrStr]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
    status: NotRequired[Status42OrStr]
