
# Room

## Structure

`Room`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number_of_nights` | `int` | Optional | The total number of nights the room is booked for.<br><br>* Format: Numeric<br>* Must be a number between 1 and 99<br>* **additionalData key:** `lodging.room[N].numberOfNights` |
| `rate` | `int` | Optional | Room rate per night, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `lodging.room[N].rate` |

## Example

```python
from adyen.models.room import Room

room = Room(
    number_of_nights=138,
    rate=46
)
```

