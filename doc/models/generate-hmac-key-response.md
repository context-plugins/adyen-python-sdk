
# Generate Hmac Key Response

*This model accepts additional fields of type Any.*

## Structure

`GenerateHmacKeyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hmac_key` | `str` | Required | The HMAC key generated for this webhook. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.generate_hmac_key_response import GenerateHmacKeyResponse

generate_hmac_key_response = GenerateHmacKeyResponse(
    hmac_key='hmacKey2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

