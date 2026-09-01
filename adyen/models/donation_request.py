from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict
from .platform_chargeback_logic import PlatformChargebackLogic, PlatformChargebackLogicDict


class DonationRequest(SdkBaseModel):
    donation_account: str = Field(alias="donationAccount")
    """The Adyen account name of the charity."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account that is used to process the payment."""

    modification_amount: Amount = Field(alias="modificationAmount")
    """The amount to be donated.The ``currency`` must match the currency used in authorisation, the ``value`` must be
    smaller than or equal to the authorised amount."""

    original_reference: Optional[str] = Field(default=UNSET, alias="originalReference")
    """The original pspReference of the payment to modify. This reference is returned in:
    * authorisation response
    * authorisation notification"""

    platform_chargeback_logic: Optional[PlatformChargebackLogic] = Field(default=UNSET, alias="platformChargebackLogic")
    """Defines how to book chargebacks when using `Adyen for Platforms
    <https://docs.adyen.com/adyen-for-platforms-model>`__."""

    reference: Optional[str] = UNSET
    """Your reference for the payment modification. This reference is visible in Customer Area and in reports. Maximum
    length: 80 characters."""


class DonationRequestDict(TypedDict):
    donation_account: str
    merchant_account: str
    modification_amount: Amount | AmountDict
    original_reference: NotRequired[str]
    platform_chargeback_logic: NotRequired[PlatformChargebackLogic | PlatformChargebackLogicDict]
    reference: NotRequired[str]
