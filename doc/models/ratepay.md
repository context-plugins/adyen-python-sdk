
# Ratepay

## Structure

`Ratepay`

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
| `mtype` | [`Type48Enum`](../../doc/models/type-48-enum.md) | Required | **ratepay**<br><br>**Default**: `"ratepay"` |

## Example

```python
from adyen.models.ratepay import Ratepay
from adyen.models.type_48_enum import Type48Enum

ratepay = Ratepay(
    mtype=Type48Enum.RATEPAY,
    billing_address='billingAddress0',
    checkout_attempt_id='checkoutAttemptId8',
    delivery_address='deliveryAddress8',
    personal_details='personalDetails0',
    recurring_detail_reference='recurringDetailReference2'
)
```

