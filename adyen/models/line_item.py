from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LineItem(SdkBaseModel):
    amount_excluding_tax: Optional[int] = Field(default=UNSET, alias="amountExcludingTax")
    """Item amount excluding the tax, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes/#minor-units>`__."""

    amount_including_tax: Optional[int] = Field(default=UNSET, alias="amountIncludingTax")
    """Item amount including the tax, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes/#minor-units>`__."""

    brand: Optional[str] = UNSET
    """Brand of the item."""

    color: Optional[str] = UNSET
    """Color of the item."""

    description: Optional[str] = UNSET
    """Description of the line item."""

    id: Optional[str] = UNSET
    """ID of the line item."""

    image_url: Optional[str] = Field(default=UNSET, alias="imageUrl")
    """Link to the picture of the purchased item."""

    item_category: Optional[str] = Field(default=UNSET, alias="itemCategory")
    """Item category, used by the payment methods PayPal and Ratepay."""

    manufacturer: Optional[str] = UNSET
    """Manufacturer of the item."""

    marketplace_seller_id: Optional[str] = Field(default=UNSET, alias="marketplaceSellerId")
    """Marketplace seller id."""

    product_url: Optional[str] = Field(default=UNSET, alias="productUrl")
    """Link to the purchased item."""

    quantity: Optional[int] = UNSET
    """Number of items."""

    receiver_email: Optional[str] = Field(default=UNSET, alias="receiverEmail")
    """Email associated with the given product in the basket (usually in electronic gift cards)."""

    return_shipping_company: Optional[str] = Field(default=UNSET, alias="returnShippingCompany")
    """Shipping company handling the return of the item."""

    return_tracking_number: Optional[str] = Field(default=UNSET, alias="returnTrackingNumber")
    """Tracking number for the return of the item."""

    return_tracking_uri: Optional[str] = Field(default=UNSET, alias="returnTrackingUri")
    """Tracking URI for the return of the item."""

    shipping_company: Optional[str] = Field(default=UNSET, alias="shippingCompany")
    """Shipping company handling the delivery of the item."""

    shipping_method: Optional[str] = Field(default=UNSET, alias="shippingMethod")
    """Shipping method used to deliver the item."""

    size: Optional[str] = UNSET
    """Size of the item."""

    sku: Optional[str] = UNSET
    """Stock keeping unit."""

    tax_amount: Optional[int] = Field(default=UNSET, alias="taxAmount")
    """Tax amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes/#minor-units>`__."""

    tax_percentage: Optional[int] = Field(default=UNSET, alias="taxPercentage")
    """Tax percentage, represented as a `basis point <https://en.wikipedia.org/wiki/Basis_point>`__ integer. For
    example:
     - **530** for 5.3% (five point three percent)
     - **2100** for 21% (twenty-one percent)"""

    tracking_number: Optional[str] = Field(default=UNSET, alias="trackingNumber")
    """Tracking number for the delivery of the item."""

    tracking_uri: Optional[str] = Field(default=UNSET, alias="trackingUri")
    """Tracking URI for the delivery of the item."""

    upc: Optional[str] = UNSET
    """Universal Product Code."""


class LineItemDict(TypedDict):
    amount_excluding_tax: NotRequired[int]
    amount_including_tax: NotRequired[int]
    brand: NotRequired[str]
    color: NotRequired[str]
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    item_category: NotRequired[str]
    manufacturer: NotRequired[str]
    marketplace_seller_id: NotRequired[str]
    product_url: NotRequired[str]
    quantity: NotRequired[int]
    receiver_email: NotRequired[str]
    return_shipping_company: NotRequired[str]
    return_tracking_number: NotRequired[str]
    return_tracking_uri: NotRequired[str]
    shipping_company: NotRequired[str]
    shipping_method: NotRequired[str]
    size: NotRequired[str]
    sku: NotRequired[str]
    tax_amount: NotRequired[int]
    tax_percentage: NotRequired[int]
    tracking_number: NotRequired[str]
    tracking_uri: NotRequired[str]
    upc: NotRequired[str]
