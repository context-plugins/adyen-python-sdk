
# Clearpay Response Info

*This model accepts additional fields of type Any.*

## Structure

`ClearpayResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `support_url` | `str` | Optional | Support Url |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.clearpay_response_info import ClearpayResponseInfo

clearpay_response_info = ClearpayResponseInfo(
    support_url='supportUrl4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

