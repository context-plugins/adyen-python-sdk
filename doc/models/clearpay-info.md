
# Clearpay Info

*This model accepts additional fields of type Any.*

## Structure

`ClearpayInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `support_url` | `str` | Required | Support Url |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.clearpay_info import ClearpayInfo

clearpay_info = ClearpayInfo(
    support_url='supportUrl6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

