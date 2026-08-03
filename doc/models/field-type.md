
# Field Type

The type of error field.

*This model accepts additional fields of type Any.*

## Structure

`FieldType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | `str` | Optional | The full name of the property. |
| `field_name` | [`FieldName`](../../doc/models/field-name.md) | Optional | - |
| `shareholder_code` | `str` | Optional | The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.field_name import FieldName
from adyen.models.field_type import FieldType

field_type = FieldType(
    field='field6',
    field_name=FieldName.ACCOUNTSTATETYPE,
    shareholder_code='shareholderCode0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

