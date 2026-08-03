
# Open Invoice

*This model accepts additional fields of type Any.*

## Structure

`OpenInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_address` | `str` | Optional | The address where to send the invoice. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `delivery_address` | `str` | Optional | The address where the goods should be delivered. |
| `personal_details` | `str` | Optional | Shopper name, date of birth, phone number, and email address. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type39`](../../doc/models/type-39.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.open_invoice import OpenInvoice

open_invoice = OpenInvoice(
    billing_address='billingAddress4',
    checkout_attempt_id='checkoutAttemptId2',
    delivery_address='deliveryAddress2',
    personal_details='personalDetails4',
    recurring_detail_reference='recurringDetailReference6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

