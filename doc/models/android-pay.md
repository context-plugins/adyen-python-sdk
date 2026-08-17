
# Android Pay

## Structure

`AndroidPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type6Enum`](../../doc/models/type-6-enum.md) | Optional | **androidpay**<br><br>**Default**: `"androidpay"` |

## Example

```python
from adyen.models.android_pay import AndroidPay
from adyen.models.type_6_enum import Type6Enum

android_pay = AndroidPay(
    checkout_attempt_id='checkoutAttemptId8',
    sdk_data='sdkData8',
    mtype=Type6Enum.ANDROIDPAY
)
```

