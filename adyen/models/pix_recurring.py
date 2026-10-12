from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount42 import Amount42, Amount42Dict
from .amount43 import Amount43, Amount43Dict
from .enums.frequency2 import Frequency2OrStr


class PixRecurring(SdkBaseModel):
    billing_date: Optional[str] = Field(default=UNSET, alias="billingDate")
    """The date on which the shopper's payment method will be charged, in YYYY-MM-DD format."""

    business_day_only: Optional[bool] = Field(default=UNSET, alias="businessDayOnly")
    """Flag used to define whether liquidation can happen only on business days"""

    ends_at: Optional[str] = Field(default=UNSET, alias="endsAt")
    """End date of the billing plan, in YYYY-MM-DD format. The end date must align with the frequency and the start date
    of the billing plan. If left blank, the subscription will continue indefinitely unless it is cancelled by the
    shopper."""

    frequency: Optional[Frequency2OrStr] = UNSET
    """The frequency at which the shopper will be charged."""

    min_amount: Optional[Amount42] = Field(default=UNSET, alias="minAmount")
    """For a billing plan where the payment amounts are variable, the minimum amount to charge the shopper for each
    recurring payment. When a shopper approves the billing plan, they can also specify a maximum amount in their banking
    app."""

    original_psp_reference: Optional[str] = Field(default=UNSET, alias="originalPspReference")
    """The pspReference for the failed recurring payment. Find this in AUTHORISATION webhook you received after the
    billing date."""

    recurring_amount: Optional[Amount43] = Field(default=UNSET, alias="recurringAmount")
    """For a billing plan where the payment amount is fixed, the amount the shopper will be charged for each recurring
    payment."""

    recurring_statement: Optional[str] = Field(default=UNSET, alias="recurringStatement")
    """The text that that will be shown on the shopper's bank statement for the recurring payments. We recommend to add
    a descriptive text about the subscription to let your shoppers recognize your recurring payments. Maximum length: 35
    characters."""

    retry_policy: Optional[bool] = Field(default=UNSET, alias="retryPolicy")
    """When set to true, you can retry for failed recurring payments. The default value is true."""

    starts_at: Optional[str] = Field(default=UNSET, alias="startsAt")
    """Start date of the billing plan, in YYYY-MM-DD format. The default value is the transaction date."""


class PixRecurringDict(TypedDict):
    billing_date: NotRequired[str]
    business_day_only: NotRequired[bool]
    ends_at: NotRequired[str]
    frequency: NotRequired[Frequency2OrStr]
    min_amount: NotRequired[Amount42Dict]
    original_psp_reference: NotRequired[str]
    recurring_amount: NotRequired[Amount43Dict]
    recurring_statement: NotRequired[str]
    retry_policy: NotRequired[bool]
    starts_at: NotRequired[str]
