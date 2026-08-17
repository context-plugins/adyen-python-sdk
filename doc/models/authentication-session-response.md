
# Authentication Session Response

## Structure

`AuthenticationSessionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the session. |
| `token` | `str` | Optional | The session token created. |

## Example

```python
from adyen.models.authentication_session_response import AuthenticationSessionResponse

authentication_session_response = AuthenticationSessionResponse(
    id='id2',
    token='token4'
)
```

