
# Web Data 1

The website and app URL of the legal entity.

*This model accepts additional fields of type Any.*

## Structure

`WebData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `web_address` | `str` | Optional | The URL of the website or the app store URL. |
| `web_address_id` | `str` | Optional, Read-only | The unique identifier of the web address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.web_data_1 import WebData1

web_data_1 = WebData1(
    web_address='webAddress4',
    web_address_id='webAddressId0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

