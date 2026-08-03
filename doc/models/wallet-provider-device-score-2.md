
# Wallet Provider Device Score 2

Wallet Provider Device Score and the operation.

Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**.

*This model accepts additional fields of type Any.*

## Structure

`WalletProviderDeviceScore2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.wallet_provider_device_score_2 import WalletProviderDeviceScore2

wallet_provider_device_score_2 = WalletProviderDeviceScore2(
    operation='operation4',
    value=164,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

