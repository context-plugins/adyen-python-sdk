from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CardIdentification2(SdkBaseModel):
    """Card details used for the transfer, such as the Primary Account Number (PAN) or stored payment method ID.
    Required if ``sourceOfFunds`` is **DEBIT**. Provide either:
     - ``storedPaymentMethodId`` or
     - ``expiryMonth``, ``expiryYear``, and ``number``."""

    expiry_month: Optional[str] = Field(default=UNSET, alias="expiryMonth")
    """The expiry month of the card.

    Format: two digits. Add a leading zero for single-digit months. For example:
    * 03 = March
    * 11 = November"""

    expiry_year: Optional[str] = Field(default=UNSET, alias="expiryYear")
    """The expiry year of the card.

    Format: four digits. For example: 2020"""

    issue_number: Optional[str] = Field(default=UNSET, alias="issueNumber")
    """The issue number of the card. Applies only to some UK debit cards."""

    number: Optional[str] = UNSET
    """The card number without any separators.

    For security, the response only includes the last four digits of the card number."""

    start_month: Optional[str] = Field(default=UNSET, alias="startMonth")
    """The month when the card was issued. Applies only to some UK debit cards.

    Format: two digits. Add a leading zero for single-digit months. For example:
    * 03 = March
    * 11 = November"""

    start_year: Optional[str] = Field(default=UNSET, alias="startYear")
    """The year when the card was issued. Applies only to some UK debit cards.

    Format: four digits. For example: 2020"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """The unique `token </payouts/payout-service/pay-out-to-cards/manage-card-information#save-card-details>`__ created
    to identify the counterparty."""


class CardIdentification2Dict(TypedDict):
    expiry_month: NotRequired[str]
    expiry_year: NotRequired[str]
    issue_number: NotRequired[str]
    number: NotRequired[str]
    start_month: NotRequired[str]
    start_year: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
