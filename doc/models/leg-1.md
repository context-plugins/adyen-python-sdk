
# Leg 1

*This model accepts additional fields of type Any.*

## Structure

`Leg1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `arrival_airport_code` | `str` | Optional | The IATA 3-letter airport code of the destination airport. This field is required if the airline data includes leg details. |
| `basic_fare_code` | `str` | Optional | The basic fare code for this leg. |
| `carrier_code` | `str` | Optional | IATA code of the carrier operating the flight. |
| `departure_airport_code` | `str` | Optional | The IATA three-letter airport code of the departure airport. This field is required if the airline data includes leg details |
| `departure_date` | `str` | Optional | The flight departure date. |
| `flight_number` | `str` | Optional | The flight identifier. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.leg_1 import Leg1

leg_1 = Leg1(
    arrival_airport_code='arrivalAirportCode4',
    basic_fare_code='basicFareCode0',
    carrier_code='carrierCode2',
    departure_airport_code='departureAirportCode0',
    departure_date='departureDate4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

