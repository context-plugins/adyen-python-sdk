from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayoutMethod(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_merchantAccount you used
    in the ``/payments`` request when you `saved the account holder's card details
    <https://docs.adyen.com/classic-platforms/payouts/manual-payout/payout-to-cards#check-and-store>`__."""

    payout_method_code: Optional[str] = Field(default=UNSET, alias="payoutMethodCode")
    """Adyen-generated unique alphanumeric identifier (UUID) for the payout method, returned in the response when you
    create a payout method. Required when updating an existing payout method in an ``/updateAccountHolder`` request."""

    payout_method_reference: Optional[str] = Field(default=UNSET, alias="payoutMethodReference")
    """Your reference for the payout method."""

    recurring_detail_reference: str = Field(alias="recurringDetailReference")
    """The
    https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_additionalData-ResponseAdditionalDataCommon-recurring-recurringDetailReference
    returned in the ``/payments`` response when you `saved the account holder's card details
    <https://docs.adyen.com/classic-platforms/payouts/manual-payout/payout-to-cards#check-and-store>`__."""

    shopper_reference: str = Field(alias="shopperReference")
    """The https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_shopperReference you
    sent in the ``/payments`` request when you `saved the account holder's card details
    <https://docs.adyen.com/classic-platforms/payouts/manual-payout/payout-to-cards#check-and-store>`__."""


class PayoutMethodDict(TypedDict):
    merchant_account: str
    payout_method_code: NotRequired[str]
    payout_method_reference: NotRequired[str]
    recurring_detail_reference: str
    shopper_reference: str
