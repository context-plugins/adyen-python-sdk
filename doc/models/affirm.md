
# Affirm

## Structure

`Affirm`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type1Enum`](../../doc/models/type-1-enum.md) | Optional | **affirm**<br><br>**Default**: `"affirm"` |

## Example

```python
from adyen.models.affirm import Affirm
from adyen.models.type_1_enum import Type1Enum

affirm = Affirm(
    checkout_attempt_id='checkoutAttemptId2',
    sdk_data='sdkData4',
    mtype=Type1Enum.AFFIRM
)
```

