from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .local_time2 import LocalTime2, LocalTime2Dict


class BalancePlatformConfiguration(SdkBaseModel):
    automatic_application: Optional[bool] = Field(default=UNSET, alias="automaticApplication")
    """Specifies whether this payout schedule is automatically applied to new balance accounts."""

    balance_platform_id: str = Field(alias="balancePlatformId")
    """The balance platform to which the payout schedule applies."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ code of the country to
    which the payout schedule applies."""

    created_at: RFC3339DateTime = Field(alias="createdAt")
    """The date when the payout schedule was created."""

    currency: Optional[str] = UNSET
    """The three-character `ISO code <https://docs.adyen.com/development-resources/currency-codes>`__ of the currency
    used for the payout schedule."""

    default_description: Optional[str] = Field(default=UNSET, alias="defaultDescription")
    """The default description for payouts initiated by this payout schedule."""

    default_frequency: Optional[str] = Field(default=UNSET, alias="defaultFrequency")
    """The default frequency of payouts initiated by this payout schedule."""

    default_frequency_value: Optional[int] = Field(default=UNSET, alias="defaultFrequencyValue")
    """The default value for date of the month or day of the week when payouts are initiated. Allowed only if
    ``defaultFrequency`` is **monthly** or **weekly**.

    Possible values if ``defaultFrequency`` is **monthly**: **[1 - 31]**.
    * If your specified date happens on a weekend, the payout is initiated on the next business day.
    * If your specified date (**29**, **30**, or **31**) does not exist in a month, the payout is initiated on the last
        day of that month.

    Possible values if ``defaultFrequency`` is **weekly**: **[1 - 5]**."""

    default_reference: Optional[str] = Field(default=UNSET, alias="defaultReference")
    """Your internal default reference for the payout schedule.When the payout schedule is applied to a balance account,
    this reference is also used for that payout schedule."""

    default_reference_for_beneficiary: Optional[str] = Field(default=UNSET, alias="defaultReferenceForBeneficiary")
    """The default reference for beneficiary for payouts initiated by this payout schedule."""

    enabled: Optional[bool] = UNSET
    """Specifies whether the payout schedule is enabled immediately after it is created."""

    id: Optional[str] = UNSET
    """The unique identifier of the payout schedule for your balance platform."""

    max_payout_amount: Optional[int] = Field(default=UNSET, alias="maxPayoutAmount")
    """The maximum amount that can be paid out from balance accounts that use this payout schedule.

    Default value: **0**, which means that there is no maximum limit."""

    min_payout_amount: Optional[int] = Field(default=UNSET, alias="minPayoutAmount")
    """The minimum amount that can be paid out from balance accounts that use this payout schedule.

    Default value: **0**."""

    payout_schedule_description: str = Field(alias="payoutScheduleDescription")
    """The type of payout schedule. This type indicates how fast funds are paid out to your user.

    Possible values:
    - **Standard**: The funds arrive in your user's transfer instrument two days after the funds are settled.
    - **Accelerated**: The funds arrive to your user's transfer instrument the day after the funds are settled."""

    retained_amount: Optional[int] = Field(default=UNSET, alias="retainedAmount")
    """The amount of funds that must remain available in a balance account after an execution of the payout schedule. If
    the funds in the balance account are less than the retained amount, the execution is not initiated.

    Default value: **0**"""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """The date when the payout schedule was updated."""

    user_settlement_delay: int = Field(alias="userSettlementDelay")
    """The default `settlement delay <https://docs.adyen.com/platforms/settle-funds/#settlement-delay>`__ for this
    payout schedule."""

    user_settlement_time: LocalTime2 = Field(alias="userSettlementTime")
    """The time when the payout funds are settled in your user's transfer instrument."""

    user_settlement_time_zone: str = Field(alias="userSettlementTimeZone")
    """The timezone of the ``userSettlementTime``."""


class BalancePlatformConfigurationDict(TypedDict):
    automatic_application: NotRequired[bool]
    balance_platform_id: str
    country_code: NotRequired[str]
    created_at: RFC3339DateTime
    currency: NotRequired[str]
    default_description: NotRequired[str]
    default_frequency: NotRequired[str]
    default_frequency_value: NotRequired[int]
    default_reference: NotRequired[str]
    default_reference_for_beneficiary: NotRequired[str]
    enabled: NotRequired[bool]
    id: NotRequired[str]
    max_payout_amount: NotRequired[int]
    min_payout_amount: NotRequired[int]
    payout_schedule_description: str
    retained_amount: NotRequired[int]
    updated_at: NotRequired[RFC3339DateTime]
    user_settlement_delay: int
    user_settlement_time: LocalTime2 | LocalTime2Dict
    user_settlement_time_zone: str
