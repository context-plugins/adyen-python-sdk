
# Car Rental

*This model accepts additional fields of type Any.*

## Structure

`CarRental`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_service_phone_number` | `str` | Optional | The customer service phone number of the car rental company.<br><br>* Format: Alphanumeric<br>* maxLength: 17<br>* For US and CA numbers must be 10 characters in length<br>* Must not contain any special characters such as + or -<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.customerServiceTollFreeNumber` |
| `no_show` | `bool` | Optional | Indicates if the customer didn't pick up their rental car.<br><br>* **additionalData key:** `carRental.noShowIndicator` |
| `pickup_info` | [`PickupInfo`](../../doc/models/pickup-info.md) | Optional | - |
| `rate_type` | [`RateType`](../../doc/models/rate-type.md) | Optional | - |
| `rental_agreement_number` | `str` | Optional | The rental agreement number for the car rental.<br><br>* Format: ASCII<br>* maxLength: 9 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.rentalAgreementNumber` |
| `rental_class_id` | `str` | Optional | The classification of the rental car.<br><br>* Format: Alphanumeric<br>* maxLength: 4 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.rentalClassId` |
| `rental_days` | `int` | Optional | The number of days the car is rented for.<br><br>* Format: Numeric<br>* Max value: 9999<br>* **additionalData key:** `carRental.daysRented` |
| `rental_rate` | `int` | Optional | Rental rate, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* Frequency of the rental rate is specified in the rateType field.<br>* **additionalData key:** `carRental.rate` |
| `rental_surcharges` | [`RentalSurcharges`](../../doc/models/rental-surcharges.md) | Optional | - |
| `renter_name` | `str` | Required | The name of the person renting the car.<br><br>* Format: ASCII<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.renterName` |
| `return_info` | [`ReturnInfo`](../../doc/models/return-info.md) | Optional | - |
| `tax_exempt` | `bool` | Optional | Indicates if the goods or services were tax-exempt, or if tax was not collected.<br><br>* **additionalData key:** `carRental.taxExemptIndicator` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.car_rental import CarRental
from adyen.models.pickup_info import PickupInfo
from adyen.models.rate_type import RateType

car_rental = CarRental(
    renter_name='renterName0',
    customer_service_phone_number='customerServicePhoneNumber6',
    no_show=False,
    pickup_info=PickupInfo(
        city='city4',
        country_code='countryCode8',
        date=dateutil.parser.parse('2016-03-13').date(),
        state_or_province='stateOrProvince4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    rate_type=RateType.DAILY,
    rental_agreement_number='rentalAgreementNumber2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

