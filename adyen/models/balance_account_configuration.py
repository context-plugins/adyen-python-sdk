from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class BalanceAccountConfiguration(SdkBaseModel):
    balance_account_id: str = Field(alias="balanceAccountId")
    """The unique identifier of the balance account to which you apply the payout schedule."""

    balance_platform_payout_schedule_id: str = Field(alias="balancePlatformPayoutScheduleId")
    """The unique identifier of the balance platform payout schedule that is applied to the balance account."""

    created_at: RFC3339DateTime = Field(alias="createdAt")
    """The date and time when the payout schedule was created."""

    currency: Optional[str] = UNSET
    """The three-character `ISO code <https://docs.adyen.com/development-resources/currency-codes>`__ of the currency
    used for this schedule."""

    description: Optional[str] = UNSET
    """The description used for all payouts initiated by this payout schedule.

    Maximum length: 140 characters. If your description is longer, it may be truncated.

    Default value: The ``defaultDescription`` from the balance platform schedule that you are applying."""

    enabled: Optional[bool] = UNSET
    """Specifies whether the payout schedule is active."""

    frequency: Optional[str] = UNSET
    """The frequency of payouts initiated by this payout schedule.

    Possible values:
    * daily
    * weekdays
    * weekly
    * monthly

    Default value: The ``defaultFrequency`` from the balance platform schedule that you are applying."""

    frequency_value: Optional[int] = Field(default=UNSET, alias="frequencyValue")
    """The date of the month or day of the week when payouts are initiated. Allowed only if ``frequency`` is **monthly**
    or **weekly**.

    Possible values if ``frequency`` is **monthly**: **[1 - 31]**.
    * If your specified date happens on a weekend, the payout is initiated on the next business day.
    * If your specified date (**29**, **30**, or **31**) does not exist in a month, the payout is initiated on the last
        day of that month.

    Possible values if ``frequency`` is **weekly**: **[1 - 5]**.

    Default value: The ``defaultFrequencyValue`` from the balance platform schedule that you are applying."""

    id: Optional[str] = UNSET
    """The unique identifier of the payout schedule for the balance account."""

    max_payout_amount: Optional[int] = Field(default=UNSET, alias="maxPayoutAmount")
    """The maximum amount that can be paid out from balance accounts that use this payout schedule.

    Default value: **0**"""

    min_payout_amount: Optional[int] = Field(default=UNSET, alias="minPayoutAmount")
    """The minimum amount that can be paid out from balance accounts that use this payout schedule.

    Default value: **0**"""

    reference: Optional[str] = UNSET
    """Your reference for the payout schedule. This reference does not appear on statements of payouts initiated by the
    payout schedule."""

    reference_for_beneficiary: Optional[str] = Field(default=UNSET, alias="referenceForBeneficiary")
    """The reference for beneficiary used for all payouts initiated by this payout schedule. This reference is sent to
    the recipient of the payout and is included in all webhooks related to the payout.

    Supported characters: **a-z**, **A-Z**, **0-9**.

    Default value: The ``defaultReferenceForBeneficiary`` from the balance platform schedule that you are applying."""

    retained_amount: Optional[int] = Field(default=UNSET, alias="retainedAmount")
    """The amount of funds that must remain available in the balance account after an execution of the payout schedule.
    If the funds in the balance account are less than the retained amount, the execution is not initiated.

    Default value: **0**"""

    sales_day_closing_time: Optional[str] = Field(default=UNSET, alias="salesDayClosingTime")
    """The time of day when the sales day is closed in balance account time zone. The sales day closing time can be
    between 00:00 to 07:00.

    Format: **HH:mm:ss**"""

    transfer_instrument_id: str = Field(alias="transferInstrumentId")
    """The unique identifier of the transfer instrument to which the funds are paid out."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """The date and time when the payout schedule was updated."""


class BalanceAccountConfigurationDict(TypedDict):
    balance_account_id: str
    balance_platform_payout_schedule_id: str
    created_at: RFC3339DateTime
    currency: NotRequired[str]
    description: NotRequired[str]
    enabled: NotRequired[bool]
    frequency: NotRequired[str]
    frequency_value: NotRequired[int]
    id: NotRequired[str]
    max_payout_amount: NotRequired[int]
    min_payout_amount: NotRequired[int]
    reference: NotRequired[str]
    reference_for_beneficiary: NotRequired[str]
    retained_amount: NotRequired[int]
    sales_day_closing_time: NotRequired[str]
    transfer_instrument_id: str
    updated_at: NotRequired[RFC3339DateTime]
