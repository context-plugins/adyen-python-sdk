
# Entry Modes Restriction 1

List of point-of-sale entry modes and the operation..

Supported operations: **anyMatch**, **noneMatch**.

*This model accepts additional fields of type Any.*

## Structure

`EntryModesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value2]`](../../doc/models/value-2.md) | Optional | List of point-of-sale entry modes.<br><br>Possible values: **barcode**, **chip**, **cof**, **contactless**, **magstripe**, **manual**, **ocr**, **server**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.entry_modes_restriction_1 import EntryModesRestriction1
from adyen.models.value_2 import Value2

entry_modes_restriction_1 = EntryModesRestriction1(
    operation='operation0',
    value=[
        Value2.UNKNOWN
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

