
# Wallet Provider Device Type

*This model accepts additional fields of type Any.*

## Structure

`WalletProviderDeviceType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value6]`](../../doc/models/value-6.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.value_6 import Value6
from adyen.models.wallet_provider_device_type import WalletProviderDeviceType

wallet_provider_device_type = WalletProviderDeviceType(
    operation='operation8',
    value=[
        Value6.TABLET_OR_EREADER,
        Value6.UNKNOWN
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

