
# Destination

*This model accepts additional fields of type Any.*

## Structure

`Destination`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_code` | `str` | Optional | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) or three-letter [ISO 3166-1 alpha-3 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) for the destination address.<br><br>* Encoding: ASCII<br>* Min length: 2 characters<br>* Max length: 3 characters<br>* **additionalData key:** `enhancedSchemeData.destinationCountryCode` |
| `postal_code` | `str` | Optional | The postal code of the destination address.<br><br>* Encoding: ASCII<br>* Max length: 10 characters<br>* Must not start with a space.<br>* For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.<br>* For Canada, it must be in 6 digits format. For example, M4B 1G5.<br>* **additionalData key:** `enhancedSchemeData.destinationPostalCode` |
| `state_or_province` | `str` | Optional | The state or province code of the destination address.<br><br>* Encoding: ASCII<br>* Max length: 3 characters<br>* Must not start with a space.<br>* **additionalData key:** `enhancedSchemeData.destinationStateProvinceCode` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.destination import Destination

destination = Destination(
    country_code='countryCode0',
    postal_code='postalCode6',
    state_or_province='stateOrProvince2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

