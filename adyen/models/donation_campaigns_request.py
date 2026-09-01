from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DonationCampaignsRequest(SdkBaseModel):
    currency: str
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes/>`__."""

    locale: Optional[str] = UNSET
    """Locale on the shopper interaction device."""

    merchant_account: str = Field(alias="merchantAccount")
    """Your merchant account identifier."""

    store: Optional[str] = UNSET
    """Required for Adyen for Platforms integrations if you are a platform model. This is your `reference
    <https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId>`__/stores#request-reference) (on
    `balance platform <https://docs.adyen.com/platforms>`__) or the `storeReference
    <https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder#request-accountHolderDetails-storeDetails-storeReference>`__
    (in the `classic integration
    <https://docs.adyen.com/classic-platforms/processing-payments/route-payment-to-store/#route-a-payment-to-a-store>`__)
    for the ecommerce or point-of-sale store that is processing the payment."""


class DonationCampaignsRequestDict(TypedDict):
    currency: str
    locale: NotRequired[str]
    merchant_account: str
    store: NotRequired[str]
