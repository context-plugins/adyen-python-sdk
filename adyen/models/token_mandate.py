from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.amount_rule import AmountRuleOrStr
from .enums.billing_attempts_rule import BillingAttemptsRuleOrStr
from .enums.frequency import FrequencyOrStr
from .enums.retry_policy import RetryPolicyOrStr


class TokenMandate(SdkBaseModel):
    account_id_type: Optional[str] = Field(default=UNSET, alias="accountIdType")
    """The type of account identifier for the masked account number."""

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

    currency: str
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__."""

    ends_at: str = Field(alias="endsAt")
    """End date of the billing plan, in YYYY-MM-DD format."""

    frequency: FrequencyOrStr
    """The frequency with which a shopper should be charged.

    Possible values: **adhoc**, **daily**, **weekly**, **biWeekly**, **monthly**, **quarterly**, **halfYearly**,
    **yearly**."""

    mandate_id: str = Field(alias="mandateId")
    """The unique identifier of the mandate."""

    masked_account_id: Optional[str] = Field(default=UNSET, alias="maskedAccountId")
    """The masked account number associated with the mandate."""

    min_amount: Optional[str] = Field(default=UNSET, alias="minAmount")
    """For a billing plan where the payment amounts are variable, the minimum amount to charge the shopper for each
    recurring payment. When a shopper approves the billing plan, they can also specify a maximum amount in their banking
    app."""

    provider_id: str = Field(alias="providerId")
    """The provider-specific identifier for this mandate."""

    recurring_amount: Optional[str] = Field(default=UNSET, alias="recurringAmount")
    """For a billing plan where the payment amount is fixed, the amount the shopper will be charged for each recurring
    payment."""

    recurring_statement: Optional[str] = Field(default=UNSET, alias="recurringStatement")
    """The text that will be shown on the shopper's bank statement for the recurring payments. We recommend to add a
    descriptive text about the subscription to let your shoppers recognize your recurring payments. Maximum length: 35
    characters."""

    remarks: Optional[str] = UNSET
    """Additional remarks or notes about the mandate."""

    retry_policy: Optional[RetryPolicyOrStr] = Field(default=UNSET, alias="retryPolicy")
    """When set to true, you can retry for failed recurring payments. The default value is true."""

    starts_at: Optional[str] = Field(default=UNSET, alias="startsAt")
    """Start date of the billing plan, in YYYY-MM-DD format. By default, the transaction date."""

    status: str
    """The status of the mandate. Examples : active, revoked, completed, expired"""

    tx_variant: str = Field(alias="txVariant")
    """The transaction variant used for this mandate."""


class TokenMandateDict(TypedDict):
    account_id_type: NotRequired[str]
    amount: str
    amount_rule: NotRequired[AmountRuleOrStr]
    billing_attempts_rule: NotRequired[BillingAttemptsRuleOrStr]
    billing_day: NotRequired[str]
    count: NotRequired[str]
    currency: str
    ends_at: str
    frequency: FrequencyOrStr
    mandate_id: str
    masked_account_id: NotRequired[str]
    min_amount: NotRequired[str]
    provider_id: str
    recurring_amount: NotRequired[str]
    recurring_statement: NotRequired[str]
    remarks: NotRequired[str]
    retry_policy: NotRequired[RetryPolicyOrStr]
    starts_at: NotRequired[str]
    status: str
    tx_variant: str
