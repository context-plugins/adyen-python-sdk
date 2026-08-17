
# Mobile Pay

## Structure

`MobilePay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type37Enum`](../../doc/models/type-37-enum.md) | Optional | **mobilepay**<br><br>**Default**: `"mobilepay"` |

## Example

```python
from adyen.models.mobile_pay import MobilePay
from adyen.models.type_37_enum import Type37Enum

mobile_pay = MobilePay(
    checkout_attempt_id='checkoutAttemptId4',
    sdk_data='sdkData2',
    mtype=Type37Enum.MOBILEPAY
)
```

