
# Wallet Provider Device Type

## Structure

`WalletProviderDeviceType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value6Enum]`](../../doc/models/value-6-enum.md) | Optional | - |

## Example

```python
from adyen.models.value_6_enum import Value6Enum
from adyen.models.wallet_provider_device_type import WalletProviderDeviceType

wallet_provider_device_type = WalletProviderDeviceType(
    operation='operation8',
    value=[
        Value6Enum.TABLET_OR_EREADER,
        Value6Enum.UNKNOWN
    ]
)
```

