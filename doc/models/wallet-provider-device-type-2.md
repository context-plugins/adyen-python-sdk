
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

## Structure

`WalletProviderDeviceType2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value6Enum]`](../../doc/models/value-6-enum.md) | Optional | - |

## Example

```python
from adyen.models.value_6_enum import Value6Enum
from adyen.models.wallet_provider_device_type_2 import WalletProviderDeviceType2

wallet_provider_device_type_2 = WalletProviderDeviceType2(
    operation='operation4',
    value=[
        Value6Enum.WATCH_OR_WRISTBAND,
        Value6Enum.WEARABLE,
        Value6Enum.CARD
    ]
)
```

