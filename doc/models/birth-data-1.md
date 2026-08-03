
# Birth Data 1

The individual's birth information.

*This model accepts additional fields of type Any.*

## Structure

`BirthData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_of_birth` | `str` | Optional | The individual's date of birth, in YYYY-MM-DD format. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.birth_data_1 import BirthData1

birth_data_1 = BirthData1(
    date_of_birth='dateOfBirth0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

