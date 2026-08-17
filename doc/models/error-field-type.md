
# Error Field Type

## Structure

`ErrorFieldType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `int` | Optional | The validation error code. |
| `error_description` | `str` | Optional | A description of the validation error. |
| `field_type` | [`FieldType`](../../doc/models/field-type.md) | Optional | The type of error field. |

## Example

```python
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType

error_field_type = ErrorFieldType(
    error_code=86,
    error_description='errorDescription8',
    field_type=FieldType(
        field='field6',
        field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
        shareholder_code='shareholderCode0'
    )
)
```

