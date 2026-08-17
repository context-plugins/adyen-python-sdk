
# Wallet Provider Device Score

## Structure

`WalletProviderDeviceScore`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | - |

## Example

```python
from adyen.models.wallet_provider_device_score import WalletProviderDeviceScore

wallet_provider_device_score = WalletProviderDeviceScore(
    operation='operation0',
    value=174
)
```

