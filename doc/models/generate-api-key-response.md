
# Generate Api Key Response

## Structure

`GenerateApiKeyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Required | The generated API key. |

## Example

```python
from adyen.models.generate_api_key_response import GenerateApiKeyResponse

generate_api_key_response = GenerateApiKeyResponse(
    api_key='apiKey6'
)
```

