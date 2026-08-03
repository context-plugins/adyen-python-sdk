
# Leg

*This model accepts additional fields of type Any.*

## Structure

`Leg`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `carrier_code` | `str` | Optional | The [IATA](https://www.iata.org/services/pages/codes.aspx) 2-letter accounting code (PAX) that identifies the carrier.<br>This field is required if the airline data includes leg details.<br><br>* Example: KLM = KL<br>* minLength: 2 characters<br>* maxLength: 2 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `airline.leg[N].carrier_code` |
| `class_of_travel` | `str` | Optional | A one-letter travel class identifier.<br>The following are common:<br><br>* F: first class<br><br>* J: business class<br><br>* Y: economy class<br><br>* W: premium economy<br><br>* Encoding: ASCII<br><br>* minLength: 1 character<br><br>* maxLength: 1 character<br><br>* Must not start with a space or be all spaces.<br><br>* Must not be all zeros.<br><br>* **additionalData key:** `airline.leg[N].class_of_travel` |
| `date_of_travel` | `datetime` | Optional | Date and time of travel in format `yyyy-MM-ddTHH:mm`.<br><br>* Use local time of departure airport.<br>* minLength: 16 characters<br>* maxLength: 16 characters<br>* **additionalData key:** `airline.leg[N].date_of_travel` |
| `departure_airport_code` | `str` | Optional | The [IATA](https://www.iata.org/services/pages/codes.aspx) three-letter airport code of the departure airport.<br>This field is required if the airline data includes leg details.<br><br>* Encoding: ASCII<br>* Example: Amsterdam = AMS<br>* minLength: 3 characters<br>* maxLength: 3 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `airline.leg[N].depart_airport` |
| `departure_tax` | `int` | Optional | The amount of [departure tax](https://en.wikipedia.org/wiki/Departure_tax) charged, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Encoding: Numeric<br>* minLength: 1<br>* maxLength: 11<br>* Must not be all zeros.<br>* **additionalData key:** `airline.leg[N].depart_tax` |
| `destination_airport_code` | `str` | Optional | The [IATA](https://www.iata.org/services/pages/codes.aspx) 3-letter airport code of the destination airport.<br>This field is required if the airline data includes leg details.<br><br>* Example: Amsterdam = AMS<br>* Encoding: ASCII<br>* minLength: 3 characters<br>* maxLength: 3 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `airline.leg[N].destination_code` |
| `fare_basis_code` | `str` | Optional | The [fare basis code](https://en.wikipedia.org/wiki/Fare_basis_code), alphanumeric.<br><br>* minLength: 1 character<br>* maxLength: 15 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `airline.leg[N].fare_base_code` |
| `flight_number` | `str` | Optional | The flight identifier.<br><br>* minLength: 1 character<br>* maxLength: 5 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `airline.leg[N].flight_number` |
| `stop_over_code` | `str` | Optional | A one-letter code that indicates whether the passenger is entitled to make a stopover. Can be a space, O if the passenger is entitled to make a stopover, or X if they are not.<br><br>* Encoding: ASCII<br>* minLength: 1 character<br>* maxLength: 1 character<br>* **additionalData key:** `airline.leg[N].stop_over_code` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.leg import Leg

leg = Leg(
    carrier_code='carrierCode0',
    class_of_travel='classOfTravel2',
    date_of_travel=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    departure_airport_code='departureAirportCode8',
    departure_tax=16,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

