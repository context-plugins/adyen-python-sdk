
# BLIK

## Structure

`BLIK`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `blik_code` | `str` | Optional | BLIK code consisting of 6 digits. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type13Enum`](../../doc/models/type-13-enum.md) | Optional | **blik** |

## Example

```python
from adyen.models.blik import BLIK

blik = BLIK(
    blik_code='blikCode0',
    checkout_attempt_id='checkoutAttemptId8',
    recurring_detail_reference='recurringDetailReference2',
    sdk_data='sdkData8',
    stored_payment_method_id='storedPaymentMethodId6'
)
```

