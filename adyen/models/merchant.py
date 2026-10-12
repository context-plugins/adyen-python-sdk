from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data_center import DataCenter, DataCenterDict
from .merchant_links2 import MerchantLinks2, MerchantLinks2Dict


class Merchant(SdkBaseModel):
    links: Optional[MerchantLinks2] = Field(default=UNSET, alias="_links")
    """References to resources connected with this merchant."""

    capture_delay: Optional[str] = Field(default=UNSET, alias="captureDelay")
    """The `capture delay <https://docs.adyen.com/online-payments/capture#capture-delay>`__ set for the merchant
    account.

    Possible values:
    * **Immediate**
    * **Manual**
    * Number of days from **1** to **29**"""

    company_id: Optional[str] = Field(default=UNSET, alias="companyId")
    """The unique identifier of the company account this merchant belongs to"""

    data_centers: Optional[list[DataCenter]] = Field(default=UNSET, alias="dataCenters")
    """List of available data centers.

    Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you
    use the live URL prefix from the data center closest to your shoppers."""

    default_shopper_interaction: Optional[str] = Field(default=UNSET, alias="defaultShopperInteraction")
    """The default https://docs.adyen.com/api-explorer/#/CheckoutService/v68/post/payments__reqParam_shopperInteraction
    value used when processing payments through this merchant account."""

    description: Optional[str] = UNSET
    """Your description for the merchant account, maximum 300 characters"""

    id: Optional[str] = UNSET
    """The unique identifier of the merchant account."""

    merchant_city: Optional[str] = Field(default=UNSET, alias="merchantCity")
    """The city where the legal entity of this merchant account is registered."""

    name: Optional[str] = UNSET
    """The name of the legal entity associated with the merchant account."""

    pricing_plan: Optional[str] = Field(default=UNSET, alias="pricingPlan")
    """Only applies to merchant accounts managed by Adyen's partners. The name of the pricing plan assigned to the
    merchant account."""

    primary_settlement_currency: Optional[str] = Field(default=UNSET, alias="primarySettlementCurrency")
    """The currency of the country where the legal entity of this merchant account is registered. Format: `ISO currency
    code <https://docs.adyen.com/development-resources/currency-codes>`__. For example, a legal entity based in the
    United States has USD as the primary settlement currency."""

    reference: Optional[str] = UNSET
    """Reference of the merchant account."""

    shop_web_address: Optional[str] = Field(default=UNSET, alias="shopWebAddress")
    """The URL for the ecommerce website used with this merchant account."""

    status: Optional[str] = UNSET
    """The status of the merchant account.

    Possible values:

    * **PreActive**: The merchant account has been created. Users cannot access the merchant account in the Customer
        Area. The account cannot process payments.
    * **Active**: Users can access the merchant account in the Customer Area. If the company account is also **Active**,
        then payment processing and payouts are enabled.
    * **InactiveWithModifications**: Users can access the merchant account in the Customer Area. You cannot process new
        payments but you can still modify payments, for example issue refunds. You can still receive payouts.
    * **Inactive**: Users can access the merchant account in the Customer Area. Payment processing and payouts are
        disabled.
    * **Closed**: The account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts
        are disabled."""


class MerchantDict(TypedDict):
    links: NotRequired[MerchantLinks2Dict]
    capture_delay: NotRequired[str]
    company_id: NotRequired[str]
    data_centers: NotRequired[list[DataCenterDict]]
    default_shopper_interaction: NotRequired[str]
    description: NotRequired[str]
    id: NotRequired[str]
    merchant_city: NotRequired[str]
    name: NotRequired[str]
    pricing_plan: NotRequired[str]
    primary_settlement_currency: NotRequired[str]
    reference: NotRequired[str]
    shop_web_address: NotRequired[str]
    status: NotRequired[str]
