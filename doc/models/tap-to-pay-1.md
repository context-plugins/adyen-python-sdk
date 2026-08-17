
# Tap to Pay 1

Settings for Tap to Pay.

## Structure

`TapToPay1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_display_name` | `str` | Optional | The text shown on the screen during the Tap to Pay transaction. |

## Example

```python
from adyen.models.tap_to_pay_1 import TapToPay1

tap_to_pay_1 = TapToPay1(
    merchant_display_name='merchantDisplayName6'
)
```

