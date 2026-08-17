
# Lodging 1

## Structure

`Lodging1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `check_in_date` | `str` | Optional | The check-in date. |
| `number_of_nights` | `int` | Optional | The total number of nights the room is booked for. |

## Example

```python
from adyen.models.lodging_1 import Lodging1

lodging_1 = Lodging1(
    check_in_date='checkInDate0',
    number_of_nights=52
)
```

