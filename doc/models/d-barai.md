
# D Barai

## Structure

`DBarai`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type20Enum`](../../doc/models/type-20-enum.md) | Optional | **dbarai**<br><br>**Default**: `"dbarai"` |

## Example

```python
from adyen.models.d_barai import DBarai
from adyen.models.type_20_enum import Type20Enum

d_barai = DBarai(
    checkout_attempt_id='checkoutAttemptId6',
    recurring_detail_reference='recurringDetailReference0',
    sdk_data='sdkData0',
    stored_payment_method_id='storedPaymentMethodId4',
    mtype=Type20Enum.DBARAI
)
```

