
# Generate Client Key Response

*This model accepts additional fields of type Any.*

## Structure

`GenerateClientKeyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_key` | `str` | Required | Generated client key |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.generate_client_key_response import GenerateClientKeyResponse

generate_client_key_response = GenerateClientKeyResponse(
    client_key='clientKey8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

