
# Lodging

*This model accepts additional fields of type Any.*

## Structure

`Lodging`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `check_in_date` | `date` | Optional | The check-in date.<br><br>* Min Length: 10 characters<br>* Max Length: 10 characters<br>* Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd<br>* **additionalData key:** `lodging.checkInDate` |
| `check_out_date` | `date` | Optional | The check-out date.<br><br>* Min Length: 10 characters<br>* Max Length: 10 characters<br>* Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd<br>* **additionalData key:** `lodging.checkOutDate` |
| `customer_service_phone_number` | `str` | Optional | The toll-free phone number for the lodging customer service.<br><br>* Format: Alphanumeric<br>* For US and CA numbers must be 10 characters in length<br>* Must not start with a space<br>* Must not contain any special characters such as + or -<br>* Must not be all zeros.<br>* **additionalData key:** `lodging.customerServiceTollFreeNumber` |
| `fire_safety_compliance` | `bool` | Optional | Indicates that the facility complies with the Hotel and Motel Fire Safety Act of 1990.<br><br>* **additionalData key:** `lodging.fireSafetyActIndicator` |
| `folio` | [`Folio`](../../doc/models/folio.md) | Optional | - |
| `food_beverage_charges` | `int` | Optional | Any charges for food and beverages associated with the booking, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `lodging.foodBeverageCharges` |
| `lodging_charge_type` | [`LodgingChargeType`](../../doc/models/lodging-charge-type.md) | Optional | - |
| `no_show` | `bool` | Optional | Indicates if the customer didn't check in for their booking.<br><br>* **additionalData key:** `lodging.noShowIndicator` |
| `prepaid_expenses` | `int` | Optional | The prepaid expenses for the booking, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `lodging.prepaidExpenses` |
| `property_phone_number` | `str` | Optional | The lodging property location's phone number.<br><br>* Format: Alphanumeric<br>* Min length: 10 characters<br>* For US and CA numbers must be 10 characters in length<br>* Must not start with a space<br>* Must not contain any special characters such as + or -<br>* Must not be all zeros.<br>* **additionalData key:** `lodging.propertyPhoneNumber` |
| `renter_name` | `str` | Optional | The name of the person renting the room.<br><br>* Format: ASCII<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `lodging.renterName` |
| `rooms` | [`List[Room]`](../../doc/models/room.md) | Optional | The list of rooms booked. |
| `total_room_tax` | `int` | Optional | The total room tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `lodging.totalRoomTax` |
| `total_tax` | `int` | Optional | The total tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `lodging.totalTax` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.folio import Folio
from adyen.models.lodging import Lodging

lodging = Lodging(
    check_in_date=dateutil.parser.parse('2016-03-13').date(),
    check_out_date=dateutil.parser.parse('2016-03-13').date(),
    customer_service_phone_number='customerServicePhoneNumber6',
    fire_safety_compliance=False,
    folio=Folio(
        cash_advances=122,
        number='number8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

