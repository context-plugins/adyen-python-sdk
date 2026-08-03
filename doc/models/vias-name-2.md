
# Vias Name 2

The name of the individual.

> Make sure your account holder registers using the name shown on their Photo ID.
> Maximum length: 80 characters
> Cannot contain numbers. /n Cannot be empty.

*This model accepts additional fields of type Any.*

## Structure

`ViasName2`

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
from adyen.models.vias_name_2 import ViasName2

vias_name_2 = ViasName2(
    first_name='firstName2',
    gender=Gender.FEMALE,
    infix='infix4',
    last_name='lastName6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

