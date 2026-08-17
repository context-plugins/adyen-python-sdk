
# Airline

## Structure

`Airline`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agency` | [`Agency`](../../doc/models/agency.md) | Optional | - |
| `boarding_fee` | `int` | Optional | The amount charged for boarding the plane, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Encoding: Numeric<br>* minLength: 1 character<br>* maxLength: 11 characters<br>* **additionalData key:** `airline.boarding_fee` |
| `code` | `str` | Optional | The [IATA](https://www.iata.org/services/pages/codes.aspx) 3-digit accounting code (PAX) that identifies the carrier.<br><br>* Format: IATA 3-digit accounting code (PAX)<br>* Example: KLM = 074<br>* minLength: 3 characters<br>* maxLength: 3 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `airline.airline_code` |
| `computerized_reservation_system` | `str` | Optional | The [CRS](https://en.wikipedia.org/wiki/Computer_reservation_system) used to make the reservation and purchase the ticket.<br><br>* Encoding: ASCII<br>* minLength: 4 characters<br>* maxLength: 4 characters<br>* **additionalData key:** `airline.computerized_reservation_system` |
| `customer_reference_number` | `str` | Optional | The alphanumeric customer reference number.<br><br>* Encoding: ASCII<br>* maxLength: 20 characters<br>* If you send more than 20 characters, the customer reference number is truncated<br>* Must not start with a space or be all spaces.<br>* **additionalData key:** `airline.customer_reference_number` |
| `designator_code` | `str` | Optional | The [IATA](https://www.iata.org/services/pages/codes.aspx) 2-letter accounting code (PAX) that identifies the carrier.<br><br>* Encoding: ASCII<br>* Example: KLM = KL<br>* minLength: 2 characters<br>* maxLength: 2 characters<br>* Must not start with a space or be all spaces.<br>* **additionalData key:** `airline.airline_designator_code` |
| `document_type` | `str` | Optional | A code that identifies the type of item bought. The description of the code can appear on credit card statements.<br><br>* Encoding: ASCII<br>* Example: Passenger ticket = 01<br>* minLength: 2 characters<br>* maxLength: 2 characters<br>* **additionalData key:** `airline.document_type` |
| `flight_date` | `datetime` | Optional | The flight departure date. Time is optional.<br><br>* Format for date only: `yyyy-MM-dd`<br>* Format for date and time: `yyyy-MM-ddTHH:mm`<br>* Use local time of departure airport.<br>* minLength: 10 characters<br>* maxLength: 16 characters<br>* **additionalData key:** `airline.flight_date` |
| `legs` | [`List[Leg]`](../../doc/models/leg.md) | Optional | - |
| `passenger_name` | `str` | Required | The passenger's name, initials, and title.<br><br>* Format: last name + first name or initials + title<br>* Example: *FLYER / MARY MS*<br>* minLength: 1 character<br>* maxLength: 20 characters<br>* If you send more than 20 characters, the name is truncated<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `airline.passenger_name` |
| `passengers` | [`List[Passenger]`](../../doc/models/passenger.md) | Optional | - |
| `ticket` | [`Ticket`](../../doc/models/ticket.md) | Optional | - |
| `travel_agency` | [`TravelAgency`](../../doc/models/travel-agency.md) | Optional | - |

## Example

```python
from adyen.models.agency import Agency
from adyen.models.airline import Airline

airline = Airline(
    passenger_name='passengerName0',
    agency=Agency(
        invoice_number='invoiceNumber6',
        plan_name='planName6'
    ),
    boarding_fee=160,
    code='code0',
    computerized_reservation_system='computerizedReservationSystem4',
    customer_reference_number='customerReferenceNumber6'
)
```

