
# Generate Api Key Response

*This model accepts additional fields of type Any.*

## Structure

`GenerateApiKeyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Required | The generated API key. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.generate_api_key_response import GenerateApiKeyResponse

generate_api_key_response = GenerateApiKeyResponse(
    api_key='apiKey6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

