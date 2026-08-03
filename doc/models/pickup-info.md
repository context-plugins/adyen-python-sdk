
# Pickup Info

*This model accepts additional fields of type Any.*

## Structure

`PickupInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The city where the car is rented.<br><br>* Format: ASCII<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.locationCity` |
| `country_code` | `str` | Optional | The country where the car is rented, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format.<br><br>* maxLength: 2 characters<br>* **additionalData key:** `carRental.locationCountry` |
| `date` | `date` | Optional | The pick-up date.<br><br>* minLength: 10 characters<br>* maxLength: 10 characters<br>* Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd<br>* **additionalData key:** `carRental.checkOutDate` |
| `state_or_province` | `str` | Optional | The state or province where the car is rented.<br><br>* maxLength: 3 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.locationStateProvince` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.pickup_info import PickupInfo

pickup_info = PickupInfo(
    city='city2',
    country_code='countryCode2',
    date=dateutil.parser.parse('2016-03-13').date(),
    state_or_province='stateOrProvince0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

