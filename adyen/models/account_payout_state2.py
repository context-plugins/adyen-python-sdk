from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict


class AccountPayoutState2(SdkBaseModel):
    """The payout state of the account holder."""

    allow_payout: Optional[bool] = Field(default=UNSET, alias="allowPayout")
    """Indicates whether payouts are allowed. This field is the overarching payout status, and is the aggregate of
    multiple conditions (e.g., KYC status, disabled flag, etc). If this field is false, no payouts will be permitted for
    any of the account holder's accounts. If this field is true, payouts will be permitted for any of the account
    holder's accounts."""

    disable_reason: Optional[str] = Field(default=UNSET, alias="disableReason")
    """The reason why payouts (to all of the account holder's accounts) have been disabled (by the platform). If the
    ``disabled`` field is true, this field can be used to explain why."""

    disabled: Optional[bool] = UNSET
    """Indicates whether payouts have been disabled (by the platform) for all of the account holder's accounts. A
    platform may enable and disable this field at their discretion. If this field is true, ``allowPayout`` will be false
    and no payouts will be permitted for any of the account holder's accounts. If this field is false, ``allowPayout``
    may or may not be enabled, depending on other factors."""

    not_allowed_reason: Optional[str] = Field(default=UNSET, alias="notAllowedReason")
    """The reason why payouts (to all of the account holder's accounts) have been disabled (by Adyen). If payouts have
    been disabled by Adyen, this field will explain why. If this field is blank, payouts have not been disabled by
    Adyen."""

    payout_limit: Optional[Amount] = Field(default=UNSET, alias="payoutLimit")
    """The maximum amount that payouts are limited to. Only applies if payouts are allowed but limited."""

    tier_number: Optional[int] = Field(default=UNSET, alias="tierNumber")
    """The payout tier that the account holder occupies."""


class AccountPayoutState2Dict(TypedDict):
    allow_payout: NotRequired[bool]
    disable_reason: NotRequired[str]
    disabled: NotRequired[bool]
    not_allowed_reason: NotRequired[str]
    payout_limit: NotRequired[AmountDict]
    tier_number: NotRequired[int]
