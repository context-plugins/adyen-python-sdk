
# Field Type

The type of error field.

## Structure

`FieldType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | `str` | Optional | The full name of the property. |
| `field_name` | [`FieldNameEnum`](../../doc/models/field-name-enum.md) | Optional | The type of the field. |
| `shareholder_code` | `str` | Optional | The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder. |

## Example

```python
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType

field_type = FieldType(
    field='field6',
    field_name=FieldNameEnum.ACCOUNTSTATETYPE,
    shareholder_code='shareholderCode0'
)
```

