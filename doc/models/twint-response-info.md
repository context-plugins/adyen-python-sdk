
# Twint Response Info

*This model accepts additional fields of type Any.*

## Structure

`TwintResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Optional | Twint logo. Format: Base64-encoded string. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.twint_response_info import TwintResponseInfo

twint_response_info = TwintResponseInfo(
    logo='logo6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

