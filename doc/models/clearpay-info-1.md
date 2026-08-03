
# Clearpay Info 1

Details to provide if `type` is **clearpay**.

*This model accepts additional fields of type Any.*

## Structure

`ClearpayInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `support_url` | `str` | Required | Support Url |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.clearpay_info_1 import ClearpayInfo1

clearpay_info_1 = ClearpayInfo1(
    support_url='supportUrl0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

