
# Affirm Response Info

*This model accepts additional fields of type Any.*

## Structure

`AffirmResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `public_api_key` | `str` | Optional | Affirm public API key |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.affirm_response_info import AffirmResponseInfo

affirm_response_info = AffirmResponseInfo(
    public_api_key='publicApiKey0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

