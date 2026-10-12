from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .enums.funding_source import FundingSourceOrStr
from .enums.interval import IntervalOrStr


class CapabilitySettings3(SdkBaseModel):
    """A JSON object containing the settings that are allowed for the account holder."""

    amount_per_industry: Optional[dict[str, Amount17]] = Field(default=UNSET, alias="amountPerIndustry")
    authorized_card_users: Optional[bool] = Field(default=UNSET, alias="authorizedCardUsers")
    funding_source: Optional[list[FundingSourceOrStr]] = Field(default=UNSET, alias="fundingSource")
    interval: Optional[IntervalOrStr] = UNSET
    max_amount: Optional[Amount17] = Field(default=UNSET, alias="maxAmount")


class CapabilitySettings3Dict(TypedDict):
    amount_per_industry: NotRequired[dict[str, Amount17Dict]]
    authorized_card_users: NotRequired[bool]
    funding_source: NotRequired[list[FundingSourceOrStr]]
    interval: NotRequired[IntervalOrStr]
    max_amount: NotRequired[Amount17Dict]
