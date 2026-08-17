
# Stored Payment Method 1

## Structure

`StoredPaymentMethod1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type27Enum`](../../doc/models/type-27-enum.md) | Optional | **sepadirectdebit**<br><br>**Default**: `"sepadirectdebit"` |

## Example

```python
from adyen.models.stored_payment_method_1 import StoredPaymentMethod1
from adyen.models.type_27_enum import Type27Enum

stored_payment_method_1 = StoredPaymentMethod1(
    checkout_attempt_id='checkoutAttemptId0',
    recurring_detail_reference='recurringDetailReference4',
    sdk_data='sdkData6',
    stored_payment_method_id='storedPaymentMethodId8',
    mtype=Type27Enum.SEPADIRECTDEBIT
)
```

