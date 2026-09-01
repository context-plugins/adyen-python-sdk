from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.amount_rule import AmountRuleOrStr
from .enums.billing_attempts_rule import BillingAttemptsRuleOrStr
from .enums.frequency import FrequencyOrStr


class Mandate(SdkBaseModel):
    """The mandate details to initiate recurring transaction."""

    amount: str
    """The billing amount (in minor units) of the recurring transactions."""

    amount_rule: Optional[AmountRuleOrStr] = Field(default=UNSET, alias="amountRule")
    """The limitation rule of the billing amount.

    Possible values:
     * **max**: The transaction amount can not exceed the ``amount``.

     * **exact**: The transaction amount should be the same as the ``amount``."""

    billing_attempts_rule: Optional[BillingAttemptsRuleOrStr] = Field(default=UNSET, alias="billingAttemptsRule")
    """The rule to specify the period, within which the recurring debit can happen, relative to the mandate recurring
    date.

    Possible values:

     * **on**: On a specific date.

     * **before**: Before and on a specific date.

     * **after**: On and after a specific date."""

    billing_day: Optional[str] = Field(default=UNSET, alias="billingDay")
    """The number of the day, on which the recurring debit can happen. Should be within the same calendar month as the
    mandate recurring date.

    Possible values: 1-31 based on the ``frequency``."""

    count: Optional[str] = UNSET
    """The number of transactions that can be performed within the given frequency."""

    ends_at: str = Field(alias="endsAt")
    """End date of the billing plan, in YYYY-MM-DD format."""

    frequency: FrequencyOrStr
    """The frequency with which a shopper should be charged.

    Possible values: **adhoc**, **daily**, **weekly**, **biWeekly**, **monthly**, **quarterly**, **halfYearly**,
    **yearly**."""

    remarks: Optional[str] = UNSET
    """The message shown by UPI to the shopper on the approval screen."""

    starts_at: Optional[str] = Field(default=UNSET, alias="startsAt")
    """Start date of the billing plan, in YYYY-MM-DD format. By default, the transaction date."""


class MandateDict(TypedDict):
    amount: str
    amount_rule: NotRequired[AmountRuleOrStr]
    billing_attempts_rule: NotRequired[BillingAttemptsRuleOrStr]
    billing_day: NotRequired[str]
    count: NotRequired[str]
    ends_at: str
    frequency: FrequencyOrStr
    remarks: NotRequired[str]
    starts_at: NotRequired[str]
