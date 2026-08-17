
# Afterpay

## Structure

`Afterpay`

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
| `mtype` | [`Type2Enum`](../../doc/models/type-2-enum.md) | Required | **afterpay_default**<br><br>**Default**: `"afterpay_default"` |

## Example

```python
from adyen.models.afterpay import Afterpay
from adyen.models.type_2_enum import Type2Enum

afterpay = Afterpay(
    mtype=Type2Enum.AFTERPAY_DEFAULT,
    billing_address='billingAddress8',
    checkout_attempt_id='checkoutAttemptId6',
    delivery_address='deliveryAddress6',
    personal_details='personalDetails8',
    recurring_detail_reference='recurringDetailReference0'
)
```

