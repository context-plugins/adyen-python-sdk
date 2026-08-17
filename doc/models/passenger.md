
# Passenger

## Structure

`Passenger`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_of_birth` | `date` | Optional | The passenger's date of birth.<br><br>* Format `yyyy-MM-dd`<br>* minLength: 10<br>* maxLength: 10<br>* **additionalData key:** `airline.passenger[N].date_of_birth` |
| `first_name` | `str` | Optional | The passenger's first name.<br><br>> This field is required if the airline data includes passenger details or leg details.<br><br>* Encoding: ASCII<br>* **additionalData key:** `airline.passenger[N].first_name` |
| `last_name` | `str` | Optional | The passenger's last name.<br><br>> This field is required if the airline data includes passenger details or leg details.<br><br>* Encoding: ASCII<br>* **additionalData key:** `airline.passenger[N].last_name` |
| `phone_number` | `str` | Optional | The passenger's phone number, including country code. This is an alphanumeric field that can include the '+' and '-' signs.<br><br>* Encoding: ASCII<br>* minLength: 3 characters<br>* maxLength: 30 characters<br>* **additionalData key:** `airline.passenger[N].phone_number` |
| `traveller_type` | `str` | Optional | The IATA passenger type code (PTC).<br><br>* Encoding: ASCII<br>* minLength: 3 characters<br>* maxLength: 6 characters<br>* **additionalData key:** `airline.passenger[N].traveller_type` |

## Example

```python
import dateutil.parser

from adyen.models.passenger import Passenger

passenger = Passenger(
    date_of_birth=dateutil.parser.parse('2016-03-13').date(),
    first_name='firstName6',
    last_name='lastName4',
    phone_number='phoneNumber0',
    traveller_type='travellerType8'
)
```

