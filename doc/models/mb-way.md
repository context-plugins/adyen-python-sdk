
# MB Way

## Structure

`MBWay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `shopper_email` | `str` | Required | - |
| `telephone_number` | `str` | Required | - |
| `mtype` | [`Type36Enum`](../../doc/models/type-36-enum.md) | Optional | **mbway**<br><br>**Default**: `"mbway"` |

## Example

```python
from adyen.models.mb_way import MBWay
from adyen.models.type_36_enum import Type36Enum

mb_way = MBWay(
    shopper_email='shopperEmail2',
    telephone_number='telephoneNumber6',
    checkout_attempt_id='checkoutAttemptId0',
    sdk_data='sdkData6',
    mtype=Type36Enum.MBWAY
)
```

