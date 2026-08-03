
# Updatable Address

*This model accepts additional fields of type Any.*

## Structure

`UpdatableAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The name of the city. |
| `line_1` | `str` | Optional | The street address. |
| `line_2` | `str` | Optional | Second address line. |
| `line_3` | `str` | Optional | Third address line. |
| `postal_code` | `str` | Optional | The postal code. |
| `state_or_province` | `str` | Optional | The state or province code as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada.<br><br>Required for the following countries:<br><br>- Australia<br>- Brazil<br>- Canada<br>- India<br>- Mexico<br>- New Zealand<br>- United States |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.updatable_address import UpdatableAddress

updatable_address = UpdatableAddress(
    city='city8',
    line_1='line10',
    line_2='line22',
    line_3='line30',
    postal_code='postalCode0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

