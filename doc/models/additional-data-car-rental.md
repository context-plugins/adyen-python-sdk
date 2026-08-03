
# Additional Data Car Rental

*This model accepts additional fields of type Any.*

## Structure

`AdditionalDataCarRental`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `car_rental_check_out_date` | `str` | Optional | The pick-up date.<br><br>* Date format: `yyyyMMdd` |
| `car_rental_customer_service_toll_free_number` | `str` | Optional | The customer service phone number of the car rental company.<br><br>* Format: Alphanumeric<br>* maxLength: 17<br>* For US and CA numbers must be 10 characters in length<br>* Must not start with a space<br>* Must not contain any special characters such as + or -<br>  *Must not be all zeros. |
| `car_rental_days_rented` | `str` | Optional | Number of days for which the car is being rented.<br><br>* Format: Numeric<br>* maxLength: 4<br>* Must not be all spaces |
| `car_rental_fuel_charges` | `str` | Optional | Any fuel charges associated with the rental, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Format: Numeric<br>* maxLength: 12 |
| `car_rental_insurance_charges` | `str` | Optional | Any insurance charges associated with the rental, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Format: Numeric<br>* maxLength: 12<br>* Must not be all spaces<br>  *Must not be all zeros. |
| `car_rental_location_city` | `str` | Optional | The city where the car is rented.<br><br>* Format: Alphanumeric<br>* maxLength: 18<br>* Must not start with a space or be all spaces<br>  *Must not be all zeros. |
| `car_rental_location_country` | `str` | Optional | The country where the car is rented, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format.<br><br>* Format: Alphanumeric<br>* maxLength: 2 |
| `car_rental_location_state_province` | `str` | Optional | The state or province where the car is rented.<br><br>* Format: Alphanumeric<br>* maxLength: 2<br>* Must not start with a space or be all spaces<br>  *Must not be all zeros. |
| `car_rental_no_show_indicator` | `str` | Optional | Indicates if the customer didn't pick up their rental car.<br><br>* Y - Customer did not pick up their car<br>* N - Not applicable |
| `car_rental_one_way_drop_off_charges` | `str` | Optional | The charge for not returning a car to the original rental location, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* maxLength: 12 |
| `car_rental_rate` | `str` | Optional | The daily rental rate, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* Format: Alphanumeric<br>* maxLength: 12 |
| `car_rental_rate_indicator` | `str` | Optional | Specifies whether the given rate is applied daily or weekly.<br><br>* D - Daily rate<br>* W - Weekly rate |
| `car_rental_rental_agreement_number` | `str` | Optional | The rental agreement number for the car rental.<br><br>* Format: Alphanumeric<br>* maxLength: 9<br>* Must not start with a space or be all spaces<br>  *Must not be all zeros. |
| `car_rental_rental_class_id` | `str` | Optional | The classification of the rental car.<br><br>* Format: Alphanumeric<br>* maxLength: 4<br>* Must not start with a space or be all spaces<br>  *Must not be all zeros. |
| `car_rental_renter_name` | `str` | Optional | The name of the person renting the car.<br><br>* Format: Alphanumeric<br>* maxLength: 26<br>* If you send more than 26 characters, the name is truncated<br>* Must not start with a space or be all spaces<br>  *Must not be all zeros. |
| `car_rental_return_city` | `str` | Optional | The city where the car must be returned.<br><br>* Format: Alphanumeric<br>* maxLength: 18<br>* Must not start with a space or be all spaces<br>  *Must not be all zeros. |
| `car_rental_return_country` | `str` | Optional | The country where the car must be returned, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format.<br><br>* Format: Alphanumeric<br>* maxLength: 2 |
| `car_rental_return_date` | `str` | Optional | The last date to return the car by.<br><br>* Date format: `yyyyMMdd`<br>* maxLength: 8 |
| `car_rental_return_location_id` | `str` | Optional | The agency code, phone number, or address abbreviation<br><br>* Format: Alphanumeric<br>* maxLength: 10<br>* Must not start with a space or be all spaces<br>  *Must not be all zeros. |
| `car_rental_return_state_province` | `str` | Optional | The state or province where the car must be returned.<br><br>* Format: Alphanumeric<br>* maxLength: 3<br>* Must not start with a space or be all spaces<br>  *Must not be all zeros. |
| `car_rental_tax_exempt_indicator` | `str` | Optional | Indicates if the goods or services were tax-exempt, or if tax was not paid on them.<br><br>Values:<br><br>* Y - Goods or services were tax exempt<br>* N - Tax was not collected |
| `travel_entertainment_auth_data_duration` | `str` | Optional | Number of days the car is rented for. This should be included in the auth message.<br><br>* Format: Numeric<br>* maxLength: 4 |
| `travel_entertainment_auth_data_market` | `str` | Optional | Indicates what market-specific dataset will be submitted or is being submitted. Value should be 'A' for car rental. This should be included in the auth message.<br><br>* Format: Alphanumeric<br>* maxLength: 1 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_data_car_rental import AdditionalDataCarRental

additional_data_car_rental = AdditionalDataCarRental(
    car_rental_check_out_date='carRental.checkOutDate4',
    car_rental_customer_service_toll_free_number='carRental.customerServiceTollFreeNumber6',
    car_rental_days_rented='carRental.daysRented8',
    car_rental_fuel_charges='carRental.fuelCharges4',
    car_rental_insurance_charges='carRental.insuranceCharges4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

