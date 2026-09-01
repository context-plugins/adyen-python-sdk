from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount import Amount, AmountDict


class ForexQuote1(SdkBaseModel):
    account: Optional[str] = UNSET
    """The account name."""

    account_type: Optional[str] = Field(default=UNSET, alias="accountType")
    """The account type."""

    base_amount: Optional[Amount] = Field(default=UNSET, alias="baseAmount")
    """The base amount."""

    base_points: int = Field(alias="basePoints")
    """The base points."""

    buy: Optional[Amount] = UNSET
    """The buy rate."""

    interbank: Optional[Amount] = UNSET
    """The interbank amount."""

    reference: Optional[str] = UNSET
    """The reference assigned to the forex quote request."""

    sell: Optional[Amount] = UNSET
    """The sell rate."""

    signature: Optional[str] = UNSET
    """The signature to validate the integrity."""

    source: Optional[str] = UNSET
    """The source of the forex quote."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of forex."""

    valid_till: RFC3339DateTime = Field(alias="validTill")
    """The date until which the forex quote is valid."""


class ForexQuote1Dict(TypedDict):
    account: NotRequired[str]
    account_type: NotRequired[str]
    base_amount: NotRequired[Amount | AmountDict]
    base_points: int
    buy: NotRequired[Amount | AmountDict]
    interbank: NotRequired[Amount | AmountDict]
    reference: NotRequired[str]
    sell: NotRequired[Amount | AmountDict]
    signature: NotRequired[str]
    source: NotRequired[str]
    type_: NotRequired[str]
    valid_till: RFC3339DateTime
