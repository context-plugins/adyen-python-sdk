
# Authentication Session Response

*This model accepts additional fields of type Any.*

## Structure

`AuthenticationSessionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the session. |
| `token` | `str` | Optional | The session token created. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.authentication_session_response import AuthenticationSessionResponse

authentication_session_response = AuthenticationSessionResponse(
    id='id2',
    token='token4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

