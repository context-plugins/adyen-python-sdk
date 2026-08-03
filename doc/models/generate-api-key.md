
# Generate Api Key

*This model accepts additional fields of type Any.*

## Structure

`GenerateApiKey`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.generate_api_key import GenerateApiKey

generate_api_key = GenerateApiKey(
    href='href0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

