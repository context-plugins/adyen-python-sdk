from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount import Amount, AmountDict
from .enums.delivery_address_indicator import DeliveryAddressIndicatorOrStr
from .enums.delivery_timeframe import DeliveryTimeframeOrStr


class MerchantRiskIndicator11(SdkBaseModel):
    """Additional risk fields for 3D Secure 2.
    > For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a
        frictionless flow."""

    address_match: Optional[bool] = Field(default=UNSET, alias="addressMatch")
    """Whether the chosen delivery address is identical to the billing address."""

    delivery_address_indicator: Optional[DeliveryAddressIndicatorOrStr] = Field(
        default=UNSET, alias="deliveryAddressIndicator"
    )
    """Indicator regarding the delivery address. Allowed values:
    * ``shipToBillingAddress``
    * ``shipToVerifiedAddress``
    * ``shipToNewAddress``
    * ``shipToStore``
    * ``digitalGoods``
    * ``goodsNotShipped``
    * ``other``"""

    delivery_email: Optional[str] = Field(default=UNSET, alias="deliveryEmail")
    """The delivery email address (for digital goods)."""

    delivery_email_address: Optional[str] = Field(default=UNSET, alias="deliveryEmailAddress")
    """For Electronic delivery, the email address to which the merchandise was delivered. Maximum length: 254
    characters."""

    delivery_timeframe: Optional[DeliveryTimeframeOrStr] = Field(default=UNSET, alias="deliveryTimeframe")
    """The estimated delivery time for the shopper to receive the goods. Allowed values:
    * ``electronicDelivery``
    * ``sameDayShipping``
    * ``overnightShipping``
    * ``twoOrMoreDaysShipping``"""

    gift_card_amount: Optional[Amount] = Field(default=UNSET, alias="giftCardAmount")
    """For prepaid or gift card purchase, the purchase amount total of prepaid or gift card(s)."""

    gift_card_count: Optional[int] = Field(default=UNSET, alias="giftCardCount")
    """For prepaid or gift card purchase, total count of individual prepaid or gift cards/codes purchased."""

    gift_card_curr: Optional[str] = Field(default=UNSET, alias="giftCardCurr")
    """For prepaid or gift card purchase, `ISO 4217 <https://www.iso.org/iso-4217-currency-codes.html>`__ three-digit
    currency code of the gift card, other than those listed in Table A.5 of the EMVCo 3D Secure Protocol and Core
    Functions Specification."""

    pre_order_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="preOrderDate")
    """For pre-order purchases, the expected date this product will be available to the shopper."""

    pre_order_purchase: Optional[bool] = Field(default=UNSET, alias="preOrderPurchase")
    """Indicator for whether this transaction is for pre-ordering a product."""

    pre_order_purchase_ind: Optional[str] = Field(default=UNSET, alias="preOrderPurchaseInd")
    """Indicates whether Cardholder is placing an order for merchandise with a future availability or release date."""

    reorder_items: Optional[bool] = Field(default=UNSET, alias="reorderItems")
    """Indicator for whether the shopper has already purchased the same items in the past."""

    reorder_items_ind: Optional[str] = Field(default=UNSET, alias="reorderItemsInd")
    """Indicates whether the cardholder is reordering previously purchased merchandise."""

    ship_indicator: Optional[str] = Field(default=UNSET, alias="shipIndicator")
    """Indicates shipping method chosen for the transaction."""


class MerchantRiskIndicator11Dict(TypedDict):
    address_match: NotRequired[bool]
    delivery_address_indicator: NotRequired[DeliveryAddressIndicatorOrStr]
    delivery_email: NotRequired[str]
    delivery_email_address: NotRequired[str]
    delivery_timeframe: NotRequired[DeliveryTimeframeOrStr]
    gift_card_amount: NotRequired[AmountDict]
    gift_card_count: NotRequired[int]
    gift_card_curr: NotRequired[str]
    pre_order_date: NotRequired[RFC3339DateTime]
    pre_order_purchase: NotRequired[bool]
    pre_order_purchase_ind: NotRequired[str]
    reorder_items: NotRequired[bool]
    reorder_items_ind: NotRequired[str]
    ship_indicator: NotRequired[str]
