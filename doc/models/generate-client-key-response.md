
# Generate Client Key Response

## Structure

`GenerateClientKeyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_key` | `str` | Required | Generated client key |

## Example

```python
from adyen.models.generate_client_key_response import GenerateClientKeyResponse

generate_client_key_response = GenerateClientKeyResponse(
    client_key='clientKey8'
)
```

