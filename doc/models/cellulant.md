
# Cellulant

## Structure

`Cellulant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `issuer` | `str` | Optional | The Cellulant issuer. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type17Enum`](../../doc/models/type-17-enum.md) | Optional | **Cellulant**<br><br>**Default**: `"cellulant"` |

## Example

```python
from adyen.models.cellulant import Cellulant
from adyen.models.type_17_enum import Type17Enum

cellulant = Cellulant(
    checkout_attempt_id='checkoutAttemptId6',
    issuer='issuer0',
    sdk_data='sdkData0',
    mtype=Type17Enum.CELLULANT
)
```

