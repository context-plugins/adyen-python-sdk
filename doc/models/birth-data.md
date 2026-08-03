
# Birth Data

*This model accepts additional fields of type Any.*

## Structure

`BirthData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_of_birth` | `str` | Optional | The individual's date of birth, in YYYY-MM-DD format. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.birth_data import BirthData

birth_data = BirthData(
    date_of_birth='dateOfBirth6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

