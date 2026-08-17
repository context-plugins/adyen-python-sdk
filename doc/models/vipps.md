
# Vipps

## Structure

`Vipps`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `telephone_number` | `str` | Required | - |
| `mtype` | [`Type54Enum`](../../doc/models/type-54-enum.md) | Optional | **vipps**<br><br>**Default**: `"vipps"` |

## Example

```python
from adyen.models.type_54_enum import Type54Enum
from adyen.models.vipps import Vipps

vipps = Vipps(
    telephone_number='telephoneNumber8',
    checkout_attempt_id='checkoutAttemptId2',
    recurring_detail_reference='recurringDetailReference6',
    sdk_data='sdkData4',
    stored_payment_method_id='storedPaymentMethodId0',
    mtype=Type54Enum.VIPPS
)
```

