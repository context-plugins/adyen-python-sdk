
# Line Item

*This model accepts additional fields of type Any.*

## Structure

`LineItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_excluding_tax` | `int` | Optional | Item amount excluding the tax, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
| `amount_including_tax` | `int` | Optional | Item amount including the tax, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
| `brand` | `str` | Optional | Brand of the item. |
| `color` | `str` | Optional | Color of the item. |
| `description` | `str` | Optional | Description of the line item.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `id` | `str` | Optional | ID of the line item. |
| `image_url` | `str` | Optional | Link to the picture of the purchased item. |
| `item_category` | `str` | Optional | Item category, used by the payment methods PayPal and Ratepay. |
| `manufacturer` | `str` | Optional | Manufacturer of the item. |
| `marketplace_seller_id` | `str` | Optional | Marketplace seller id. |
| `product_url` | `str` | Optional | Link to the purchased item. |
| `quantity` | `int` | Optional | Number of items. |
| `receiver_email` | `str` | Optional | Email associated with the given product in the basket (usually in electronic gift cards). |
| `return_shipping_company` | `str` | Optional | Shipping company handling the return of the item. |
| `return_tracking_number` | `str` | Optional | Tracking number for the return of the item. |
| `return_tracking_uri` | `str` | Optional | Tracking URI for the return of the item. |
| `shipping_company` | `str` | Optional | Shipping company handling the delivery of the item. |
| `shipping_method` | `str` | Optional | Shipping method used to deliver the item. |
| `size` | `str` | Optional | Size of the item. |
| `sku` | `str` | Optional | Stock keeping unit. |
| `tax_amount` | `int` | Optional | Tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
| `tax_percentage` | `int` | Optional | Tax percentage, represented as a [basis point](https://en.wikipedia.org/wiki/Basis_point) integer. For example:<br><br>- **530** for 5.3% (five point three percent)<br>- **2100** for 21% (twenty-one percent) |
| `tracking_number` | `str` | Optional | Tracking number for the delivery of the item. |
| `tracking_uri` | `str` | Optional | Tracking URI for the delivery of the item. |
| `upc` | `str` | Optional | Universal Product Code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.line_item import LineItem

line_item = LineItem(
    amount_excluding_tax=12,
    amount_including_tax=122,
    brand='brand0',
    color='color0',
    description='description6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

