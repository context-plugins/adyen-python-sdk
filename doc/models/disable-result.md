
# Disable Result

*This model accepts additional fields of type Any.*

## Structure

`DisableResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | `str` | Optional | Depending on whether a specific recurring detail was in the request, result is either [detail-successfully-disabled] or [all-details-successfully-disabled]. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.disable_result import DisableResult

disable_result = DisableResult(
    response='response6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

