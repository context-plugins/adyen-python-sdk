from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.funding_source import FundingSourceOrStr
from .enums.interval import IntervalOrStr
from .patchable_amount_dto import PatchableAmountDto, PatchableAmountDtoDict


class CapabilitySettings2(SdkBaseModel):
    amount_per_industry: Optional[dict[str, PatchableAmountDto]] = Field(default=UNSET, alias="amountPerIndustry")
    """The maximum amount a card holder can spend per industry."""

    authorized_card_users: Optional[bool] = Field(default=UNSET, alias="authorizedCardUsers")
    """The number of card holders who can use the card."""

    funding_source: Optional[list[FundingSourceOrStr]] = Field(default=UNSET, alias="fundingSource")
    """The funding source of the card, for example **debit**."""

    interval: Optional[IntervalOrStr] = UNSET
    """The period when the rule conditions apply."""

    max_amount: Optional[PatchableAmountDto] = Field(default=UNSET, alias="maxAmount")
    """The maximum amount a card holder can withdraw per day."""


class CapabilitySettings2Dict(TypedDict):
    amount_per_industry: NotRequired[dict[str, PatchableAmountDtoDict]]
    authorized_card_users: NotRequired[bool]
    funding_source: NotRequired[list[FundingSourceOrStr]]
    interval: NotRequired[IntervalOrStr]
    max_amount: NotRequired[PatchableAmountDtoDict]
