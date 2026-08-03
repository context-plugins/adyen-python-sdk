
# Allowed Origins

*This model accepts additional fields of type Any.*

## Structure

`AllowedOrigins`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.allowed_origins import AllowedOrigins

allowed_origins = AllowedOrigins(
    href='href4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

