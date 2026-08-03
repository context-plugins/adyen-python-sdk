
# Tap to Pay 1

Settings for Tap to Pay.

*This model accepts additional fields of type Any.*

## Structure

`TapToPay1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_display_name` | `str` | Optional | The text shown on the screen during the Tap to Pay transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.tap_to_pay_1 import TapToPay1

tap_to_pay_1 = TapToPay1(
    merchant_display_name='merchantDisplayName6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

