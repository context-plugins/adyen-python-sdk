
# Twint Response Info 2

**twint** details

*This model accepts additional fields of type Any.*

## Structure

`TwintResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Optional | Twint logo. Format: Base64-encoded string. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.twint_response_info_2 import TwintResponseInfo2

twint_response_info_2 = TwintResponseInfo2(
    logo='logo6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

