
# Vias Name 1

The name of the person.

*This model accepts additional fields of type Any.*

## Structure

`ViasName1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `gender` | [`Gender`](../../doc/models/gender.md) | Optional | **Constraints**: *Maximum Length*: `1` |
| `infix` | `str` | Optional | The name's infix, if applicable.<br><br>> A maximum length of twenty (20) characters is imposed.<br><br>**Constraints**: *Maximum Length*: `20` |
| `last_name` | `str` | Optional | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.gender import Gender
from adyen.models.vias_name_1 import ViasName1

vias_name_1 = ViasName1(
    first_name='firstName2',
    gender=Gender.MALE,
    infix='infix4',
    last_name='lastName6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

