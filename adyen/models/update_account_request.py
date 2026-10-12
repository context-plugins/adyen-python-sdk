from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payout_speed1 import PayoutSpeed1OrStr
from .update_payout_schedule_request2 import UpdatePayoutScheduleRequest2, UpdatePayoutScheduleRequest2Dict


class UpdateAccountRequest(SdkBaseModel):
    account_code: str = Field(alias="accountCode")
    """The code of the account to update."""

    bank_account_uuid: Optional[str] = Field(default=UNSET, alias="bankAccountUUID")
    """The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts
    in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different
    currencies will be sent to a matching bank account of the account holder."""

    description: Optional[str] = UNSET
    """A description of the account, maximum 256 characters.You can use alphanumeric characters (A-Z, a-z, 0-9), white
    spaces, and underscores ``_``."""

    metadata: Optional[dict[str, str]] = UNSET
    """A set of key and value pairs for general use by the merchant. The keys do not have specific names and may be used
    for storing miscellaneous data as desired.
    > Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of
        those key-value pairs."""

    payout_method_code: Optional[str] = Field(default=UNSET, alias="payoutMethodCode")
    """The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent
    using this payout method code."""

    payout_schedule: Optional[UpdatePayoutScheduleRequest2] = Field(default=UNSET, alias="payoutSchedule")
    """The details of the payout schedule to which the account must be updated."""

    payout_speed: Optional[PayoutSpeed1OrStr] = Field(default=UNSET, alias="payoutSpeed")
    """Speed at which payouts for this account are processed.

    Possible values: ``STANDARD`` (default), ``SAME_DAY``."""


class UpdateAccountRequestDict(TypedDict):
    account_code: str
    bank_account_uuid: NotRequired[str]
    description: NotRequired[str]
    metadata: NotRequired[dict[str, str]]
    payout_method_code: NotRequired[str]
    payout_schedule: NotRequired[UpdatePayoutScheduleRequest2Dict]
    payout_speed: NotRequired[PayoutSpeed1OrStr]
