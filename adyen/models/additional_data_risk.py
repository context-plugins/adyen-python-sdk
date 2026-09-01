from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataRisk(SdkBaseModel):
    riskdata_custom_field_name: Optional[str] = Field(default=UNSET, alias="riskdata.[customFieldName]")
    """The data for your custom risk field. For more information, refer to `Create custom risk fields
    <https://docs.adyen.com/risk-management/configure-custom-risk-rules#step-1-create-custom-risk-fields>`__."""

    riskdata_basket_item_item_nr_amount_per_item: Optional[str] = Field(
        default=UNSET, alias="riskdata.basket.item[itemNr].amountPerItem"
    )
    """The price of item in the basket, represented in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    riskdata_basket_item_item_nr_brand: Optional[str] = Field(default=UNSET, alias="riskdata.basket.item[itemNr].brand")
    """Brand of the item."""

    riskdata_basket_item_item_nr_category: Optional[str] = Field(
        default=UNSET, alias="riskdata.basket.item[itemNr].category"
    )
    """Category of the item."""

    riskdata_basket_item_item_nr_color: Optional[str] = Field(default=UNSET, alias="riskdata.basket.item[itemNr].color")
    """Color of the item."""

    riskdata_basket_item_item_nr_currency: Optional[str] = Field(
        default=UNSET, alias="riskdata.basket.item[itemNr].currency"
    )
    """The three-character `ISO currency code <https://en.wikipedia.org/wiki/ISO_4217>`__."""

    riskdata_basket_item_item_nr_item_id: Optional[str] = Field(
        default=UNSET, alias="riskdata.basket.item[itemNr].itemID"
    )
    """ID of the item."""

    riskdata_basket_item_item_nr_manufacturer: Optional[str] = Field(
        default=UNSET, alias="riskdata.basket.item[itemNr].manufacturer"
    )
    """Manufacturer of the item."""

    riskdata_basket_item_item_nr_product_title: Optional[str] = Field(
        default=UNSET, alias="riskdata.basket.item[itemNr].productTitle"
    )
    """A text description of the product the invoice line refers to."""

    riskdata_basket_item_item_nr_quantity: Optional[str] = Field(
        default=UNSET, alias="riskdata.basket.item[itemNr].quantity"
    )
    """Quantity of the item purchased."""

    riskdata_basket_item_item_nr_receiver_email: Optional[str] = Field(
        default=UNSET, alias="riskdata.basket.item[itemNr].receiverEmail"
    )
    """Email associated with the given product in the basket (usually in electronic gift cards)."""

    riskdata_basket_item_item_nr_size: Optional[str] = Field(default=UNSET, alias="riskdata.basket.item[itemNr].size")
    """Size of the item."""

    riskdata_basket_item_item_nr_sku: Optional[str] = Field(default=UNSET, alias="riskdata.basket.item[itemNr].sku")
    """`Stock keeping unit <https://en.wikipedia.org/wiki/Stock_keeping_unit>`__."""

    riskdata_basket_item_item_nr_upc: Optional[str] = Field(default=UNSET, alias="riskdata.basket.item[itemNr].upc")
    """`Universal Product Code <https://en.wikipedia.org/wiki/Universal_Product_Code>`__."""

    riskdata_promotions_promotion_item_nr_promotion_code: Optional[str] = Field(
        default=UNSET, alias="riskdata.promotions.promotion[itemNr].promotionCode"
    )
    """Code of the promotion."""

    riskdata_promotions_promotion_item_nr_promotion_discount_amount: Optional[str] = Field(
        default=UNSET, alias="riskdata.promotions.promotion[itemNr].promotionDiscountAmount"
    )
    """The discount amount of the promotion, represented in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    riskdata_promotions_promotion_item_nr_promotion_discount_currency: Optional[str] = Field(
        default=UNSET, alias="riskdata.promotions.promotion[itemNr].promotionDiscountCurrency"
    )
    """The three-character `ISO currency code <https://en.wikipedia.org/wiki/ISO_4217>`__."""

    riskdata_promotions_promotion_item_nr_promotion_discount_percentage: Optional[str] = Field(
        default=UNSET, alias="riskdata.promotions.promotion[itemNr].promotionDiscountPercentage"
    )
    """Promotion's percentage discount. It is represented in percentage value and there is no need to include the '%'
    sign.

    e.g. for a promotion discount of 30%, the value of the field should be 30."""

    riskdata_promotions_promotion_item_nr_promotion_name: Optional[str] = Field(
        default=UNSET, alias="riskdata.promotions.promotion[itemNr].promotionName"
    )
    """Name of the promotion."""

    riskdata_risk_profile_reference: Optional[str] = Field(default=UNSET, alias="riskdata.riskProfileReference")
    """Reference number of the risk profile that you want to apply to the payment. If not provided or left blank, the
    merchant-level account's default risk profile will be applied to the payment. For more information, see `dynamically
    assign a risk profile to a payment
    <https://docs.adyen.com/risk-management/create-and-use-risk-profiles#dynamically-assign-a-risk-profile-to-a-payment>`__."""

    riskdata_skip_risk: Optional[str] = Field(default=UNSET, alias="riskdata.skipRisk")
    """If this parameter is provided with the value **true**, risk checks for the payment request are skipped and the
    transaction will not get a risk score."""


class AdditionalDataRiskDict(TypedDict):
    riskdata_custom_field_name: NotRequired[str]
    riskdata_basket_item_item_nr_amount_per_item: NotRequired[str]
    riskdata_basket_item_item_nr_brand: NotRequired[str]
    riskdata_basket_item_item_nr_category: NotRequired[str]
    riskdata_basket_item_item_nr_color: NotRequired[str]
    riskdata_basket_item_item_nr_currency: NotRequired[str]
    riskdata_basket_item_item_nr_item_id: NotRequired[str]
    riskdata_basket_item_item_nr_manufacturer: NotRequired[str]
    riskdata_basket_item_item_nr_product_title: NotRequired[str]
    riskdata_basket_item_item_nr_quantity: NotRequired[str]
    riskdata_basket_item_item_nr_receiver_email: NotRequired[str]
    riskdata_basket_item_item_nr_size: NotRequired[str]
    riskdata_basket_item_item_nr_sku: NotRequired[str]
    riskdata_basket_item_item_nr_upc: NotRequired[str]
    riskdata_promotions_promotion_item_nr_promotion_code: NotRequired[str]
    riskdata_promotions_promotion_item_nr_promotion_discount_amount: NotRequired[str]
    riskdata_promotions_promotion_item_nr_promotion_discount_currency: NotRequired[str]
    riskdata_promotions_promotion_item_nr_promotion_discount_percentage: NotRequired[str]
    riskdata_promotions_promotion_item_nr_promotion_name: NotRequired[str]
    riskdata_risk_profile_reference: NotRequired[str]
    riskdata_skip_risk: NotRequired[str]
