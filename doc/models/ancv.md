
# ANCV

## Structure

`ANCV`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `beneficiary_id` | `str` | Optional | ANCV account identification (email or account number) |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type5Enum`](../../doc/models/type-5-enum.md) | Optional | **ancv** |

## Example

```python
from adyen.models.ancv import ANCV

ancv = ANCV(
    beneficiary_id='beneficiaryId6',
    checkout_attempt_id='checkoutAttemptId4',
    recurring_detail_reference='recurringDetailReference8',
    sdk_data='sdkData2',
    stored_payment_method_id='storedPaymentMethodId2'
)
```

