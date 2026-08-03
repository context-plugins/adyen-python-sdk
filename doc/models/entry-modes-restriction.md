
# Entry Modes Restriction

*This model accepts additional fields of type Any.*

## Structure

`EntryModesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value2]`](../../doc/models/value-2.md) | Optional | List of point-of-sale entry modes.<br><br>Possible values: **barcode**, **chip**, **cof**, **contactless**, **magstripe**, **manual**, **ocr**, **server**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.entry_modes_restriction import EntryModesRestriction
from adyen.models.value_2 import Value2

entry_modes_restriction = EntryModesRestriction(
    operation='operation8',
    value=[
        Value2.CHIP,
        Value2.COF,
        Value2.CONTACTLESS
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

