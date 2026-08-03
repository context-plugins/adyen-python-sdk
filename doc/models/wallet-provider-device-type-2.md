
# Wallet Provider Device Type 2

Wallet Provider Device Type and the operation.

Supported operations: **anyMatch**, **noneMatch**.

Supported value inputs:

- **MOBILE_PHONE**

- **TABLET_OR_EREADER**

- **WATCH_OR_WRISTBAND**

- **WEARABLE**

- **CARD**

- **PC**

- **OTHER**

- **UNKNOWN**

*This model accepts additional fields of type Any.*

## Structure

`WalletProviderDeviceType2`

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
from adyen.models.wallet_provider_device_type_2 import WalletProviderDeviceType2

wallet_provider_device_type_2 = WalletProviderDeviceType2(
    operation='operation4',
    value=[
        Value6.WATCH_OR_WRISTBAND,
        Value6.WEARABLE,
        Value6.CARD
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

