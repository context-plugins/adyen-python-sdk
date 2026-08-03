
# Card Holder Pin

*This model accepts additional fields of type Any.*

## Structure

`CardHolderPin`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `encr_pin_block` | `str` | Required | - |
| `pin_format` | [`PinFormat1`](../../doc/models/pin-format-1.md) | Required | - |
| `additional_input` | `str` | Optional | **Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_holder_pin import CardHolderPin
from adyen.models.pin_format_1 import PinFormat1

card_holder_pin = CardHolderPin(
    encr_pin_block='EncrPINBlock2',
    pin_format=PinFormat1.ISO2,
    additional_input='AdditionalInput2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

