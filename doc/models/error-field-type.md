
# Error Field Type

*This model accepts additional fields of type Any.*

## Structure

`ErrorFieldType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `int` | Optional | The validation error code. |
| `error_description` | `str` | Optional | A description of the validation error. |
| `field_type` | [`FieldType2`](../../doc/models/field-type-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name import FieldName
from adyen.models.field_type_2 import FieldType2

error_field_type = ErrorFieldType(
    error_code=86,
    error_description='errorDescription8',
    field_type=FieldType2(
        field='field6',
        field_name=FieldName.DRIVINGLICENCEFRONT,
        shareholder_code='shareholderCode0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

