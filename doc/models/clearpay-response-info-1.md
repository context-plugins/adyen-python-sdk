
# Clearpay Response Info 1

**clearpay** details

*This model accepts additional fields of type Any.*

## Structure

`ClearpayResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `support_url` | `str` | Optional | Support Url |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.clearpay_response_info_1 import ClearpayResponseInfo1

clearpay_response_info_1 = ClearpayResponseInfo1(
    support_url='supportUrl6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

