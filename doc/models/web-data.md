
# Web Data

*This model accepts additional fields of type Any.*

## Structure

`WebData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `web_address` | `str` | Optional | The URL of the website or the app store URL. |
| `web_address_id` | `str` | Optional, Read-only | The unique identifier of the web address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.web_data import WebData

web_data = WebData(
    web_address='webAddress8',
    web_address_id='webAddressId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

