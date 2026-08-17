
# Additional Data Open Invoice

## Structure

`AdditionalDataOpenInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `openinvoicedata_merchant_data` | `str` | Optional | Holds different merchant data points like product, purchase, customer, and so on. It takes data in a Base64 encoded string.<br><br>The `merchantData` parameter needs to be added to the `openinvoicedata` signature at the end.<br><br>Since the field is optional, if it's not included it does not impact computing the merchant signature.<br><br>Applies only to Klarna.<br><br>You can contact Klarna for the format and structure of the string. |
| `openinvoicedata_number_of_lines` | `str` | Optional | The number of invoice lines included in `openinvoicedata`.<br><br>There needs to be at least one line, so `numberOfLines` needs to be at least 1. |
| `openinvoicedata_recipient_first_name` | `str` | Optional | First name of the recipient. If the delivery address and the billing address are different, specify the `recipientFirstName` and `recipientLastName` to share the delivery address with Klarna. Otherwise, only the billing address is shared with Klarna. |
| `openinvoicedata_recipient_last_name` | `str` | Optional | Last name of the recipient. If the delivery address and the billing address are different, specify the `recipientFirstName` and `recipientLastName` to share the delivery address with Klarna. Otherwise, only the billing address is shared with Klarna. |
| `openinvoicedata_line_item_nr_currency_code` | `str` | Optional | The three-character ISO currency code. |
| `openinvoicedata_line_item_nr_description` | `str` | Optional | A text description of the product the invoice line refers to. |
| `openinvoicedata_line_item_nr_item_amount` | `str` | Optional | The price for one item in the invoice line, represented in minor units.<br><br>The due amount for the item, VAT excluded. |
| `openinvoicedata_line_item_nr_item_id` | `str` | Optional | A unique id for this item. Required for RatePay if the description of each item is not unique. |
| `openinvoicedata_line_item_nr_item_vat_amount` | `str` | Optional | The VAT due for one item in the invoice line, represented in minor units. |
| `openinvoicedata_line_item_nr_item_vat_percentage` | `str` | Optional | The VAT percentage for one item in the invoice line, represented in minor units.<br><br>For example, 19% VAT is specified as 1900. |
| `openinvoicedata_line_item_nr_number_of_items` | `str` | Optional | The number of units purchased of a specific product. |
| `openinvoicedata_line_item_nr_return_shipping_company` | `str` | Optional | Name of the shipping company handling the the return shipment. |
| `openinvoicedata_line_item_nr_return_tracking_number` | `str` | Optional | The tracking number for the return of the shipment. |
| `openinvoicedata_line_item_nr_return_tracking_uri` | `str` | Optional | URI where the customer can track the return of their shipment. |
| `openinvoicedata_line_item_nr_shipping_company` | `str` | Optional | Name of the shipping company handling the delivery. |
| `openinvoicedata_line_item_nr_shipping_method` | `str` | Optional | Shipping method. |
| `openinvoicedata_line_item_nr_tracking_number` | `str` | Optional | The tracking number for the shipment. |
| `openinvoicedata_line_item_nr_tracking_uri` | `str` | Optional | URI where the customer can track their shipment. |

## Example

```python
from adyen.models.additional_data_open_invoice import AdditionalDataOpenInvoice

additional_data_open_invoice = AdditionalDataOpenInvoice(
    openinvoicedata_merchant_data='openinvoicedata.merchantData4',
    openinvoicedata_number_of_lines='openinvoicedata.numberOfLines0',
    openinvoicedata_recipient_first_name='openinvoicedata.recipientFirstName4',
    openinvoicedata_recipient_last_name='openinvoicedata.recipientLastName2',
    openinvoicedata_line_item_nr_currency_code=Liquid error: Value cannot be null. (Parameter 'key')
)
```

