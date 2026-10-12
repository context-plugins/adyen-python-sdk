from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card import Card, CardDict


class ScheduleAccountUpdaterRequest(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be required for a particular request."""

    card: Optional[Card] = UNSET
    """Credit card data.

    Optional if ``shopperReference`` and ``selectedRecurringDetailReference`` are provided."""

    merchant_account: str = Field(alias="merchantAccount")
    """Account of the merchant."""

    reference: str
    """A reference that merchants can apply for the call."""

    selected_recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="selectedRecurringDetailReference")
    """The selected detail recurring reference.

    Optional if ``card`` is provided."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """The reference of the shopper that owns the recurring contract.

    Optional if ``card`` is provided."""


class ScheduleAccountUpdaterRequestDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    card: NotRequired[CardDict]
    merchant_account: str
    reference: str
    selected_recurring_detail_reference: NotRequired[str]
    shopper_reference: NotRequired[str]
