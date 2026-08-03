
# Airline 2

*This model accepts additional fields of type Any.*

## Structure

`Airline2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `legs` | [`List[Leg1]`](../../doc/models/leg-1.md) | Optional | Details about the flight legs for this ticket. |
| `ticket_number` | `str` | Optional | The ticket's unique identifier |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.airline_2 import Airline2
from adyen.models.leg_1 import Leg1

airline_2 = Airline2(
    legs=[
        Leg1(
            arrival_airport_code='arrivalAirportCode8',
            basic_fare_code='basicFareCode4',
            carrier_code='carrierCode6',
            departure_airport_code='departureAirportCode4',
            departure_date='departureDate8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    ticket_number='ticketNumber6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

