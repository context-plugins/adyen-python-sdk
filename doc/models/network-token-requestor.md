
# Network Token Requestor

*This model accepts additional fields of type Any.*

## Structure

`NetworkTokenRequestor`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The id of the network token requestor. |
| `name` | `str` | Optional | The name of the network token requestor. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.network_token_requestor import NetworkTokenRequestor

network_token_requestor = NetworkTokenRequestor(
    id='id8',
    name='name8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

