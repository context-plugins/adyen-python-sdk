from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payout_speed4 import PayoutSpeed4OrStr
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict
from .payout_schedule_response3 import PayoutScheduleResponse3, PayoutScheduleResponse3Dict


class UpdateAccountResponse(SdkBaseModel):
    account_code: str = Field(alias="accountCode")
    """The code of the account."""

    bank_account_uuid: Optional[str] = Field(default=UNSET, alias="bankAccountUUID")
    """The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts
    in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different
    currencies will be sent to a matching bank account of the account holder."""

    description: Optional[str] = UNSET
    """The description of the account."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """A list of fields that caused the ``/updateAccount`` request to fail."""

    metadata: Optional[dict[str, str]] = UNSET
    """A set of key and value pairs containing metadata."""

    payout_method_code: Optional[str] = Field(default=UNSET, alias="payoutMethodCode")
    """The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent
    using this payout method code."""

    payout_schedule: Optional[PayoutScheduleResponse3] = Field(default=UNSET, alias="payoutSchedule")
    """The details of the payout schedule to which the account is updated."""

    payout_speed: Optional[PayoutSpeed4OrStr] = Field(default=UNSET, alias="payoutSpeed")
    """Speed at which payouts for this account are processed.

    Possible values: ``STANDARD``, ``SAME_DAY``."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class UpdateAccountResponseDict(TypedDict):
    account_code: str
    bank_account_uuid: NotRequired[str]
    description: NotRequired[str]
    invalid_fields: NotRequired[list[ErrorFieldTypeDict]]
    metadata: NotRequired[dict[str, str]]
    payout_method_code: NotRequired[str]
    payout_schedule: NotRequired[PayoutScheduleResponse3Dict]
    payout_speed: NotRequired[PayoutSpeed4OrStr]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
