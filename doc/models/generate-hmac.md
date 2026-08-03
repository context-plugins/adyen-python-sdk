
# Generate Hmac

*This model accepts additional fields of type Any.*

## Structure

`GenerateHmac`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.generate_hmac import GenerateHmac

generate_hmac = GenerateHmac(
    href='href8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

