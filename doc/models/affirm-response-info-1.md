
# Affirm Response Info 1

*affirm** details

*This model accepts additional fields of type Any.*

## Structure

`AffirmResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `public_api_key` | `str` | Optional | Affirm public API key |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.affirm_response_info_1 import AffirmResponseInfo1

affirm_response_info_1 = AffirmResponseInfo1(
    public_api_key='publicApiKey8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

