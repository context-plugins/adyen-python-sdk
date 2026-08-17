
# Tap to Pay

## Structure

`TapToPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_display_name` | `str` | Optional | The text shown on the screen during the Tap to Pay transaction. |

## Example

```python
from adyen.models.tap_to_pay import TapToPay

tap_to_pay = TapToPay(
    merchant_display_name='merchantDisplayName8'
)
```

