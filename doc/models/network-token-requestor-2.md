
# Network Token Requestor 2

The token requestor is an entity who requested tokenization of the card for secure payments.

*This model accepts additional fields of type Any.*

## Structure

`NetworkTokenRequestor2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The id of the network token requestor. |
| `name` | `str` | Optional | The name of the network token requestor. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.network_token_requestor_2 import NetworkTokenRequestor2

network_token_requestor_2 = NetworkTokenRequestor2(
    id='id2',
    name='name2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

