from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payout_speed import PayoutSpeedOrStr
from .payout_schedule_response4 import PayoutScheduleResponse4, PayoutScheduleResponse4Dict


class Account(SdkBaseModel):
    account_code: Optional[str] = Field(default=UNSET, alias="accountCode")
    """The code of the account."""

    bank_account_uuid: Optional[str] = Field(default=UNSET, alias="bankAccountUUID")
    """The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts
    in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different
    currencies will be sent to a matching bank account of the account holder."""

    beneficiary_account: Optional[str] = Field(default=UNSET, alias="beneficiaryAccount")
    """The beneficiary of the account."""

    beneficiary_merchant_reference: Optional[str] = Field(default=UNSET, alias="beneficiaryMerchantReference")
    """The reason that a beneficiary has been set up for this account. This may have been supplied during the setup of a
    beneficiary at the discretion of the executing user."""

    description: Optional[str] = UNSET
    """A description of the account."""

    metadata: Optional[dict[str, str]] = UNSET
    """A set of key and value pairs for general use by the merchant. The keys do not have specific names and may be used
    for storing miscellaneous data as desired.
    > Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of
        those key-value pairs."""

    payout_method_code: Optional[str] = Field(default=UNSET, alias="payoutMethodCode")
    """The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent
    using this payout method code."""

    payout_schedule: Optional[PayoutScheduleResponse4] = Field(default=UNSET, alias="payoutSchedule")
    """The account's payout schedule."""

    payout_speed: Optional[PayoutSpeedOrStr] = Field(default=UNSET, alias="payoutSpeed")
    """Speed with which payouts for this account are processed. Permitted values: ``STANDARD``, ``SAME_DAY``."""

    status: Optional[str] = UNSET
    """The status of the account. Possible values: ``Active``, ``Inactive``, ``Suspended``, ``Closed``."""


class AccountDict(TypedDict):
    account_code: NotRequired[str]
    bank_account_uuid: NotRequired[str]
    beneficiary_account: NotRequired[str]
    beneficiary_merchant_reference: NotRequired[str]
    description: NotRequired[str]
    metadata: NotRequired[dict[str, str]]
    payout_method_code: NotRequired[str]
    payout_schedule: NotRequired[PayoutScheduleResponse4Dict]
    payout_speed: NotRequired[PayoutSpeedOrStr]
    status: NotRequired[str]
