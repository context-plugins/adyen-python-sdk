from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payout_schedule import PayoutScheduleOrStr
from .enums.payout_speed1 import PayoutSpeed1OrStr


class CreateAccountRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of Account Holder under which to create the account."""

    bank_account_uuid: Optional[str] = Field(default=UNSET, alias="bankAccountUUID")
    """The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts
    in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different
    currencies will be sent to a matching bank account of the account holder."""

    description: Optional[str] = UNSET
    """A description of the account, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white
    spaces, and underscores ``_``."""

    metadata: Optional[dict[str, str]] = UNSET
    """A set of key and value pairs for general use by the merchant. The keys do not have specific names and may be used
    for storing miscellaneous data as desired.
    > Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of
        those key-value pairs."""

    payout_method_code: Optional[str] = Field(default=UNSET, alias="payoutMethodCode")
    """The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent
    using this payout method code."""

    payout_schedule: Optional[PayoutScheduleOrStr] = Field(default=UNSET, alias="payoutSchedule")
    """The payout schedule for the account.

    Possible values: ``DEFAULT``, ``DAILY``, ``DAILY_US``, ``DAILY_EU``, ``DAILY_AU``, ``DAILY_SG``, ``WEEKLY``,
    ``WEEKLY_ON_TUE_FRI_MIDNIGHT``, ``BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT``, ``MONTHLY``, ``HOLD``.
    > ``HOLD`` prevents scheduled payouts, but you can still initiate payouts manually."""

    payout_schedule_reason: Optional[str] = Field(default=UNSET, alias="payoutScheduleReason")
    """The reason for the payout schedule choice.
    > This field is required when the ``payoutSchedule`` parameter is set to ``HOLD``."""

    payout_speed: Optional[PayoutSpeed1OrStr] = Field(default=UNSET, alias="payoutSpeed")
    """Speed at which payouts for this account are processed.

    Possible values: ``STANDARD`` (default), ``SAME_DAY``."""


class CreateAccountRequestDict(TypedDict):
    account_holder_code: str
    bank_account_uuid: NotRequired[str]
    description: NotRequired[str]
    metadata: NotRequired[dict[str, str]]
    payout_method_code: NotRequired[str]
    payout_schedule: NotRequired[PayoutScheduleOrStr]
    payout_schedule_reason: NotRequired[str]
    payout_speed: NotRequired[PayoutSpeed1OrStr]
