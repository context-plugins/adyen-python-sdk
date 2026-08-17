
# Additional Data Airline

## Structure

`AdditionalDataAirline`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `airline_agency_invoice_number` | `str` | Optional | The reference number for the invoice, issued by the agency.<br><br>* Encoding: ASCII<br>* minLength: 1 character<br>* maxLength: 6 characters |
| `airline_agency_plan_name` | `str` | Optional | The two-letter agency plan identifier.<br><br>* Encoding: ASCII<br>* minLength: 2 characters<br>* maxLength: 2 characters |
| `airline_airline_code` | `str` | Optional | The [IATA](https://www.iata.org/services/pages/codes.aspx) 3-digit accounting code (PAX) that identifies the carrier.<br><br>* Format: IATA 3-digit accounting code (PAX)<br>* Example: KLM = 074<br>* minLength: 3 characters<br>* maxLength: 3 characters<br>* Must not be all spaces<br>* Must not be all zeros. |
| `airline_airline_designator_code` | `str` | Optional | The [IATA](https://www.iata.org/services/pages/codes.aspx) 2-letter accounting code (PAX) that identifies the carrier.<br><br>* Encoding: ASCII<br>* Example: KLM = KL<br>* minLength: 2 characters<br>* maxLength: 2 characters<br>* Must not be all spaces<br>* Must not be all zeros. |
| `airline_boarding_fee` | `str` | Optional | The amount charged for boarding the plane, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Encoding: Numeric<br>* minLength: 1 character<br>* maxLength: 18 characters |
| `airline_computerized_reservation_system` | `str` | Optional | The [CRS](https://en.wikipedia.org/wiki/Computer_reservation_system) used to make the reservation and purchase the ticket.<br><br>* Encoding: ASCII<br>* minLength: 4 characters<br>* maxLength: 4 characters |
| `airline_customer_reference_number` | `str` | Optional | The alphanumeric customer reference number.<br><br>* Encoding: ASCII<br>* maxLength: 20 characters<br>* If you send more than 20 characters, the customer reference number is truncated<br>* Must not be all spaces |
| `airline_document_type` | `str` | Optional | A code that identifies the type of item bought. The description of the code can appear on credit card statements.<br><br>* Encoding: ASCII<br>* Example: Passenger ticket = 01<br>* minLength: 2 characters<br>* maxLength: 2 characters |
| `airline_flight_date` | `str` | Optional | The flight departure date. Local time `(HH:mm)` is optional.<br><br>* Date format: `yyyy-MM-dd`<br>* Date and time format: `yyyy-MM-dd HH:mm`<br>* minLength: 10 characters<br>* maxLength: 16 characters |
| `airline_issue_date` | `str` | Optional | The date that the ticket was issued to the passenger.<br><br>* minLength: 6 characters<br>* maxLength: 6 characters<br>* Date format: YYMMDD |
| `airline_leg_carrier_code` | `str` | Optional | The [IATA](https://www.iata.org/services/pages/codes.aspx) 2-letter accounting code (PAX) that identifies the carrier.<br>This field is required if the airline data includes leg details.<br><br>* Example: KLM = KL<br>* minLength: 2 characters<br>* maxLength: 2 characters<br>* Must not be all spaces<br>* Must not be all zeros. |
| `airline_leg_class_of_travel` | `str` | Optional | A one-letter travel class identifier.<br>The following are common:<br><br>* F: first class<br><br>* J: business class<br><br>* Y: economy class<br><br>* W: premium economy<br><br>* Encoding: ASCII<br><br>* minLength: 1 character<br><br>* maxLength: 1 character<br><br>* Must not be all spaces<br><br>* Must not be all zeros. |
| `airline_leg_date_of_travel` | `str` | Optional | Date and time of travel in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format `yyyy-MM-dd HH:mm`.<br><br>* Encoding: ASCII<br>* minLength: 16 characters<br>* maxLength: 16 characters |
| `airline_leg_depart_airport` | `str` | Optional | The [IATA](https://www.iata.org/services/pages/codes.aspx) three-letter airport code of the departure airport.<br>This field is required if the airline data includes leg details.<br><br>* Encoding: ASCII<br>* Example: Amsterdam = AMS<br>* minLength: 3 characters<br>* maxLength: 3 characters<br>* Must not be all spaces<br>* Must not be all zeros. |
| `airline_leg_depart_tax` | `str` | Optional | The amount of [departure tax](https://en.wikipedia.org/wiki/Departure_tax) charged, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Encoding: Numeric<br>* minLength: 1<br>* maxLength: 12<br>* Must not be all zeros. |
| `airline_leg_destination_code` | `str` | Optional | The [IATA](https://www.iata.org/services/pages/codes.aspx) 3-letter airport code of the destination airport.<br>This field is required if the airline data includes leg details.<br><br>* Example: Amsterdam = AMS<br>* Encoding: ASCII<br>* minLength: 3 characters<br>* maxLength: 3 characters<br>* Must not be all spaces<br>* Must not be all zeros. |
| `airline_leg_fare_base_code` | `str` | Optional | The [fare basis code](https://en.wikipedia.org/wiki/Fare_basis_code), alphanumeric.<br><br>* minLength: 1 character<br>* maxLength: 15 characters<br>* Must not be all spaces<br>* Must not be all zeros. |
| `airline_leg_flight_number` | `str` | Optional | The flight identifier.<br><br>* minLength: 1 character<br>* maxLength: 5 characters<br>* Must not be all spaces<br>* Must not be all zeros. |
| `airline_leg_stop_over_code` | `str` | Optional | A one-letter code that indicates whether the passenger is entitled to make a stopover. Can be a space, O if the passenger is entitled to make a stopover, or X if they are not.<br><br>* Encoding: ASCII<br>* minLength: 1 character<br>* maxLength: 1 character |
| `airline_passenger_date_of_birth` | `str` | Optional | The passenger's date of birth.<br><br>Date format: `yyyy-MM-dd`<br><br>* minLength: 10<br>* maxLength: 10 |
| `airline_passenger_first_name` | `str` | Optional | The passenger's first name.<br><br>> This field is required if the airline data includes passenger details or leg details.<br><br>* Encoding: ASCII |
| `airline_passenger_last_name` | `str` | Optional | The passenger's last name.<br><br>> This field is required if the airline data includes passenger details or leg details.<br><br>* Encoding: ASCII |
| `airline_passenger_phone_number` | `str` | Optional | The passenger's phone number, including country code. This is an alphanumeric field that can include the '+' and '-' signs.<br><br>* Encoding: ASCII<br>* minLength: 3 characters<br>* maxLength: 30 characters |
| `airline_passenger_traveller_type` | `str` | Optional | The IATA passenger type code (PTC).<br><br>* Encoding: ASCII<br>* minLength: 3 characters<br>* maxLength: 6 characters |
| `airline_passenger_name` | `str` | Required | The passenger's name, initials, and title.<br><br>* Format: last name + first name or initials + title<br>* Example: *FLYER / MARY MS*<br>* minLength: 1 character<br>* maxLength: 20 characters<br>* If you send more than 20 characters, the name is truncated<br>* Must not be all spaces<br>* Must not be all zeros. |
| `airline_ticket_issue_address` | `str` | Optional | The address of the organization that issued the ticket.<br><br>* minLength: 0 characters<br>* maxLength: 16 characters |
| `airline_ticket_number` | `str` | Optional | The ticket's unique identifier.<br><br>* minLength: 1 character<br>* maxLength: 15 characters<br>* Must not be all spaces<br>* Must not be all zeros. |
| `airline_travel_agency_code` | `str` | Optional | The unique identifier from IATA or ARC for the travel agency that issues the ticket.<br><br>* Encoding: ASCII<br>* minLength: 1 character<br>* maxLength: 8 characters<br>* Must not be all spaces<br>* Must not be all zeros. |
| `airline_travel_agency_name` | `str` | Optional | The name of the travel agency.<br><br>* Encoding: ASCII<br>* minLength: 1 character<br>* maxLength: 25 characters<br>* Must not be all spaces<br>* Must not be all zeros. |

## Example

```python
from adyen.models.additional_data_airline import AdditionalDataAirline

additional_data_airline = AdditionalDataAirline(
    airline_passenger_name='airline.passenger_name6',
    airline_agency_invoice_number='airline.agency_invoice_number8',
    airline_agency_plan_name='airline.agency_plan_name0',
    airline_airline_code='airline.airline_code6',
    airline_airline_designator_code='airline.airline_designator_code8',
    airline_boarding_fee='airline.boarding_fee6'
)
```

