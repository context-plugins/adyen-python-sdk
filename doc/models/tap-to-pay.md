
# Tap to Pay

*This model accepts additional fields of type Any.*

## Structure

`TapToPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_display_name` | `str` | Optional | The text shown on the screen during the Tap to Pay transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.tap_to_pay import TapToPay

tap_to_pay = TapToPay(
    merchant_display_name='merchantDisplayName8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

