
# Lodging 1

*This model accepts additional fields of type Any.*

## Structure

`Lodging1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `check_in_date` | `str` | Optional | The check-in date. |
| `number_of_nights` | `int` | Optional | The total number of nights the room is booked for. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.lodging_1 import Lodging1

lodging_1 = Lodging1(
    check_in_date='checkInDate0',
    number_of_nights=52,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

