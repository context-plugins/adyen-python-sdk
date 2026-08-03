
# Terminal Models Response

*This model accepts additional fields of type Any.*

## Structure

`TerminalModelsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[NetworkTokenRequestor]`](../../doc/models/network-token-requestor.md) | Optional | The terminal models that the API credential has access to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.network_token_requestor import NetworkTokenRequestor
from adyen.models.terminal_models_response import TerminalModelsResponse

terminal_models_response = TerminalModelsResponse(
    data=[
        NetworkTokenRequestor(
            id='id0',
            name='name0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        NetworkTokenRequestor(
            id='id0',
            name='name0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

