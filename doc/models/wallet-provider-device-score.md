
# Wallet Provider Device Score

*This model accepts additional fields of type Any.*

## Structure

`WalletProviderDeviceScore`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.wallet_provider_device_score import WalletProviderDeviceScore

wallet_provider_device_score = WalletProviderDeviceScore(
    operation='operation0',
    value=174,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

