
# Additional Data Lodging

## Structure

`AdditionalDataLodging`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lodging_special_program_code` | `str` | Optional | A code that corresponds to the category of lodging charges for the payment. Possible values:<br><br>* 1: Lodging<br>* 2: No show reservation<br>* 3: Advanced deposit |
| `lodging_check_in_date` | `str` | Optional | The arrival date.<br><br>* Date format: **yyyyMmDd**. For example, for 2023 April 22, **20230422**. |
| `lodging_check_out_date` | `str` | Optional | The departure date.<br><br>* Date format: **yyyyMmDd**. For example, for 2023 April 22, **20230422**. |
| `lodging_customer_service_toll_free_number` | `str` | Optional | The toll-free phone number for the lodging.<br><br>* Format: numeric<br>* Max length: 17 characters.<br>* For US and CA numbers must be 10 characters in length<br>* Must not start with a space<br>* Must not contain any special characters such as + or -<br>* Must not be all zeros. |
| `lodging_fire_safety_act_indicator` | `str` | Optional | Identifies that the facility complies with the Hotel and Motel Fire Safety Act of 1990. Must be 'Y' or 'N'.<br><br>* Format: alphabetic<br>* Max length: 1 character |
| `lodging_folio_cash_advances` | `str` | Optional | The folio cash advances, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Format: numeric<br>* Max length: 12 characters |
| `lodging_folio_number` | `str` | Optional | The card acceptor’s internal invoice or billing ID reference number.<br><br>* Max length: 25 characters<br>* Must not start with a space<br>* Must not contain any special characters<br>* Must not be all zeros. |
| `lodging_food_beverage_charges` | `str` | Optional | Any charges for food and beverages associated with the booking, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Format: numeric<br>* Max length: 12 characters |
| `lodging_no_show_indicator` | `str` | Optional | Indicates if the customer didn't check in for their booking.<br>Possible values:<br><br>* **Y**: the customer didn't check in<br>* **N**: the customer checked in |
| `lodging_prepaid_expenses` | `str` | Optional | The prepaid expenses for the booking.<br><br>* Format: numeric<br>* Max length: 12 characters |
| `lodging_property_phone_number` | `str` | Optional | The lodging property location's phone number.<br><br>* Format: numeric<br>* Min length: 10 characters<br>* Max length: 17 characters<br>* For US and CA numbers must be 10 characters in length<br>* Must not start with a space<br>* Must not contain any special characters such as + or -<br>* Must not be all zeros. |
| `lodging_room_1_number_of_nights` | `str` | Optional | The total number of nights the room is booked for.<br><br>* Format: numeric<br>* Must be a number between 0 and 99<br>* Max length: 4 characters |
| `lodging_room_1_rate` | `str` | Optional | The rate for the room, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Format: numeric<br>* Max length: 12 characters<br>* Must not be a negative number |
| `lodging_total_room_tax` | `str` | Optional | The total room tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Format: numeric<br>* Max length: 12 characters<br>* Must not be a negative number |
| `lodging_total_tax` | `str` | Optional | The total tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Format: numeric<br>* Max length: 12 characters<br>* Must not be a negative number |
| `travel_entertainment_auth_data_duration` | `str` | Optional | The number of nights. This should be included in the auth message.<br><br>* Format: numeric<br>* Max length: 4 characters |
| `travel_entertainment_auth_data_market` | `str` | Optional | Indicates what market-specific dataset will be submitted. Must be 'H' for Hotel. This should be included in the auth message.<br><br>* Format: alphanumeric<br>* Max length: 1 character |

## Example

```python
from adyen.models.additional_data_lodging import AdditionalDataLodging

additional_data_lodging = AdditionalDataLodging(
    lodging_special_program_code='lodging.SpecialProgramCode2',
    lodging_check_in_date='lodging.checkInDate6',
    lodging_check_out_date='lodging.checkOutDate0',
    lodging_customer_service_toll_free_number='lodging.customerServiceTollFreeNumber8',
    lodging_fire_safety_act_indicator='lodging.fireSafetyActIndicator8'
)
```

