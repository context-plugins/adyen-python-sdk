from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount3 import Amount3, Amount3Dict
from .amount4 import Amount4, Amount4Dict
from .amount5 import Amount5, Amount5Dict
from .amount6 import Amount6, Amount6Dict


class ForexQuote(SdkBaseModel):
    account: Optional[str] = UNSET
    """The account name."""

    account_type: Optional[str] = Field(default=UNSET, alias="accountType")
    """The account type."""

    base_amount: Optional[Amount3] = Field(default=UNSET, alias="baseAmount")
    """The base amount."""

    base_points: int = Field(alias="basePoints")
    """The base points."""

    buy: Optional[Amount4] = UNSET
    """The buy rate."""

    interbank: Optional[Amount5] = UNSET
    """The interbank amount."""

    reference: Optional[str] = UNSET
    """The reference assigned to the forex quote request."""

    sell: Optional[Amount6] = UNSET
    """The sell rate."""

    signature: Optional[str] = UNSET
    """The signature to validate the integrity."""

    source: Optional[str] = UNSET
    """The source of the forex quote."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of forex."""

    valid_till: RFC3339DateTime = Field(alias="validTill")
    """The date until which the forex quote is valid."""


class ForexQuoteDict(TypedDict):
    account: NotRequired[str]
    account_type: NotRequired[str]
    base_amount: NotRequired[Amount3 | Amount3Dict]
    base_points: int
    buy: NotRequired[Amount4 | Amount4Dict]
    interbank: NotRequired[Amount5 | Amount5Dict]
    reference: NotRequired[str]
    sell: NotRequired[Amount6 | Amount6Dict]
    signature: NotRequired[str]
    source: NotRequired[str]
    type_: NotRequired[str]
    valid_till: RFC3339DateTime
