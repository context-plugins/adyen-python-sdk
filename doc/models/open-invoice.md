
# Open Invoice

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
| `mtype` | [`Type39Enum`](../../doc/models/type-39-enum.md) | Optional | **openinvoice**<br><br>**Default**: `"openinvoice"` |

## Example

```python
from adyen.models.open_invoice import OpenInvoice
from adyen.models.type_39_enum import Type39Enum

open_invoice = OpenInvoice(
    billing_address='billingAddress4',
    checkout_attempt_id='checkoutAttemptId2',
    delivery_address='deliveryAddress2',
    personal_details='personalDetails4',
    recurring_detail_reference='recurringDetailReference6',
    mtype=Type39Enum.OPENINVOICE
)
```

