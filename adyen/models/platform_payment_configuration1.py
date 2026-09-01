from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class PlatformPaymentConfiguration1(SdkBaseModel):
    """Contains key-value pairs to configure the sales day closing time and settlement delay for a balance account."""

    sales_day_closing_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="salesDayClosingTime")
    """Specifies at what time a sales day ends for this account.

    Possible values: Time in **"HH:MM"** format. **HH** ranges from **00** to **07**. **MM** must be **00**.

    Default value: **"00:00"**."""

    settlement_delay_days: Optional[int] = Field(default=UNSET, alias="settlementDelayDays")
    """Specifies after how many business days the funds in a settlement batch are made available in this balance
    account. Requires Custom Sales Day Payout to be enabled for your balance account. Contact your account manager or
    implementation manager to enable this.

    Possible values: **1** to **20**, or **null**.

    Default value: **null**."""


class PlatformPaymentConfiguration1Dict(TypedDict):
    sales_day_closing_time: NotRequired[RFC3339DateTime]
    settlement_delay_days: NotRequired[int]
