from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataOpenInvoice(SdkBaseModel):
    openinvoicedata_merchant_data: Optional[str] = Field(default=UNSET, alias="openinvoicedata.merchantData")
    """Holds different merchant data points like product, purchase, customer, and so on. It takes data in a Base64
    encoded string.

    The ``merchantData`` parameter needs to be added to the ``openinvoicedata`` signature at the end.

    Since the field is optional, if it's not included it does not impact computing the merchant signature.

    Applies only to Klarna.

    You can contact Klarna for the format and structure of the string."""

    openinvoicedata_number_of_lines: Optional[str] = Field(default=UNSET, alias="openinvoicedata.numberOfLines")
    """The number of invoice lines included in ``openinvoicedata``.

    There needs to be at least one line, so ``numberOfLines`` needs to be at least 1."""

    openinvoicedata_recipient_first_name: Optional[str] = Field(
        default=UNSET, alias="openinvoicedata.recipientFirstName"
    )
    """First name of the recipient. If the delivery address and the billing address are different, specify the
    ``recipientFirstName`` and ``recipientLastName`` to share the delivery address with Klarna. Otherwise, only the
    billing address is shared with Klarna."""

    openinvoicedata_recipient_last_name: Optional[str] = Field(default=UNSET, alias="openinvoicedata.recipientLastName")
    """Last name of the recipient. If the delivery address and the billing address are different, specify the
    ``recipientFirstName`` and ``recipientLastName`` to share the delivery address with Klarna. Otherwise, only the
    billing address is shared with Klarna."""

    openinvoicedata_line_item_nr_currency_code: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].currencyCode"
    )
    """The three-character ISO currency code."""

    openinvoicedata_line_item_nr_description: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].description"
    )
    """A text description of the product the invoice line refers to."""

    openinvoicedata_line_item_nr_item_amount: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].itemAmount"
    )
    """The price for one item in the invoice line, represented in minor units.

    The due amount for the item, VAT excluded."""

    openinvoicedata_line_item_nr_item_id: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].itemId"
    )
    """A unique id for this item. Required for RatePay if the description of each item is not unique."""

    openinvoicedata_line_item_nr_item_vat_amount: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].itemVatAmount"
    )
    """The VAT due for one item in the invoice line, represented in minor units."""

    openinvoicedata_line_item_nr_item_vat_percentage: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].itemVatPercentage"
    )
    """The VAT percentage for one item in the invoice line, represented in minor units.

    For example, 19% VAT is specified as 1900."""

    openinvoicedata_line_item_nr_number_of_items: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].numberOfItems"
    )
    """The number of units purchased of a specific product."""

    openinvoicedata_line_item_nr_return_shipping_company: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].returnShippingCompany"
    )
    """Name of the shipping company handling the the return shipment."""

    openinvoicedata_line_item_nr_return_tracking_number: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].returnTrackingNumber"
    )
    """The tracking number for the return of the shipment."""

    openinvoicedata_line_item_nr_return_tracking_uri: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].returnTrackingUri"
    )
    """URI where the customer can track the return of their shipment."""

    openinvoicedata_line_item_nr_shipping_company: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].shippingCompany"
    )
    """Name of the shipping company handling the delivery."""

    openinvoicedata_line_item_nr_shipping_method: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].shippingMethod"
    )
    """Shipping method."""

    openinvoicedata_line_item_nr_tracking_number: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].trackingNumber"
    )
    """The tracking number for the shipment."""

    openinvoicedata_line_item_nr_tracking_uri: Optional[str] = Field(
        default=UNSET, alias="openinvoicedataLine[itemNr].trackingUri"
    )
    """URI where the customer can track their shipment."""


class AdditionalDataOpenInvoiceDict(TypedDict):
    openinvoicedata_merchant_data: NotRequired[str]
    openinvoicedata_number_of_lines: NotRequired[str]
    openinvoicedata_recipient_first_name: NotRequired[str]
    openinvoicedata_recipient_last_name: NotRequired[str]
    openinvoicedata_line_item_nr_currency_code: NotRequired[str]
    openinvoicedata_line_item_nr_description: NotRequired[str]
    openinvoicedata_line_item_nr_item_amount: NotRequired[str]
    openinvoicedata_line_item_nr_item_id: NotRequired[str]
    openinvoicedata_line_item_nr_item_vat_amount: NotRequired[str]
    openinvoicedata_line_item_nr_item_vat_percentage: NotRequired[str]
    openinvoicedata_line_item_nr_number_of_items: NotRequired[str]
    openinvoicedata_line_item_nr_return_shipping_company: NotRequired[str]
    openinvoicedata_line_item_nr_return_tracking_number: NotRequired[str]
    openinvoicedata_line_item_nr_return_tracking_uri: NotRequired[str]
    openinvoicedata_line_item_nr_shipping_company: NotRequired[str]
    openinvoicedata_line_item_nr_shipping_method: NotRequired[str]
    openinvoicedata_line_item_nr_tracking_number: NotRequired[str]
    openinvoicedata_line_item_nr_tracking_uri: NotRequired[str]
