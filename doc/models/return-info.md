
# Return Info

*This model accepts additional fields of type Any.*

## Structure

`ReturnInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The city where the car must be returned.<br><br>* Format: ASCII<br>* maxLength: 18 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.returnCity` |
| `country_code` | `str` | Optional | The country where the car must be returned, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format.<br><br>* maxLength: 2 characters<br>* **additionalData key:** `carRental.returnCountry` |
| `date` | `date` | Optional | The date by which the car must be returned.<br><br>* minLength: 10 characters<br>* maxLength: 10 characters<br>* Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd<br>* **additionalData key:** `carRental.returnDate` |
| `location_id` | `str` | Optional | The agency code, phone number, or address abbreviation.<br><br>* Format: ASCII<br>* maxLength: 10 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.returnLocationId` |
| `state_or_province` | `str` | Optional | The state or province where the car must be returned.<br><br>* Format: ASCII<br>* maxLength: 3 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `carRental.returnStateProvince` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.return_info import ReturnInfo

return_info = ReturnInfo(
    city='city2',
    country_code='countryCode2',
    date=dateutil.parser.parse('2016-03-13').date(),
    location_id='locationId4',
    state_or_province='stateOrProvince0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

