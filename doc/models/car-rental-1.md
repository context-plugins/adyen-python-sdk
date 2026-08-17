
# Car Rental 1

[Car rental enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/car-rental/) that may be required for processing the transaction and/or for interchange savings.

## Structure

`CarRental1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_service_phone_number` | `str` | Optional | The customer service phone number of the car rental company.<br><br>* Format: Alphanumeric<br>* maxLength: 17<br>* For US and CA numbers must be 10 characters in length<br>* Must not contain any special characters such as + or -<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.customerServiceTollFreeNumber` |
| `no_show` | `bool` | Optional | Indicates if the customer didn't pick up their rental car.<br><br>* **additionalData key:** `carRental.noShowIndicator` |
| `pickup_info` | [`PickupInfo`](../../doc/models/pickup-info.md) | Optional | - |
| `rate_type` | [`RateTypeEnum`](../../doc/models/rate-type-enum.md) | Optional | Indicates whether the rental rate is daily or weekly.<br><br>* **additionalData key:** `carRental.rateIndicator` |
| `rental_agreement_number` | `str` | Optional | The rental agreement number for the car rental.<br><br>* Format: ASCII<br>* maxLength: 9 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.rentalAgreementNumber` |
| `rental_class_id` | `str` | Optional | The classification of the rental car.<br><br>* Format: Alphanumeric<br>* maxLength: 4 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.rentalClassId` |
| `rental_days` | `int` | Optional | The number of days the car is rented for.<br><br>* Format: Numeric<br>* Max value: 9999<br>* **additionalData key:** `carRental.daysRented` |
| `rental_rate` | `int` | Optional | Rental rate, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* Frequency of the rental rate is specified in the rateType field.<br>* **additionalData key:** `carRental.rate` |
| `rental_surcharges` | [`RentalSurcharges`](../../doc/models/rental-surcharges.md) | Optional | - |
| `renter_name` | `str` | Required | The name of the person renting the car.<br><br>* Format: ASCII<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.renterName` |
| `return_info` | [`ReturnInfo`](../../doc/models/return-info.md) | Optional | - |
| `tax_exempt` | `bool` | Optional | Indicates if the goods or services were tax-exempt, or if tax was not collected.<br><br>* **additionalData key:** `carRental.taxExemptIndicator` |

## Example

```python
import dateutil.parser

from adyen.models.car_rental_1 import CarRental1
from adyen.models.pickup_info import PickupInfo
from adyen.models.rate_type_enum import RateTypeEnum

car_rental_1 = CarRental1(
    renter_name='renterName8',
    customer_service_phone_number='customerServicePhoneNumber4',
    no_show=False,
    pickup_info=PickupInfo(
        city='city4',
        country_code='countryCode8',
        date=dateutil.parser.parse('2016-03-13').date(),
        state_or_province='stateOrProvince4'
    ),
    rate_type=RateTypeEnum.DAILY,
    rental_agreement_number='rentalAgreementNumber0'
)
```

