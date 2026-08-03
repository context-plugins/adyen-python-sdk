
# Twint Info 2

Details to provide if `type` is **twint**.

*This model accepts additional fields of type Any.*

## Structure

`TwintInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Required | Twint logo. Format: Base64-encoded string. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.twint_info_2 import TwintInfo2

twint_info_2 = TwintInfo2(
    logo='logo0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

