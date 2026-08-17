
# Twint

## Structure

`Twint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `subtype` | `str` | Optional | The type of flow to initiate. |
| `mtype` | [`Type53Enum`](../../doc/models/type-53-enum.md) | Optional | The payment method type. |

## Example

```python
from adyen.models.twint import Twint

twint = Twint(
    checkout_attempt_id='checkoutAttemptId4',
    recurring_detail_reference='recurringDetailReference8',
    sdk_data='sdkData2',
    stored_payment_method_id='storedPaymentMethodId2',
    subtype='subtype0'
)
```

