
# Sub Input Detail

*This model accepts additional fields of type Any.*

## Structure

`SubInputDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `configuration` | `Dict[str, str]` | Optional | Configuration parameters for the required input. |
| `items` | [`List[NetworkTokenRequestor]`](../../doc/models/network-token-requestor.md) | Optional | In case of a select, the items to choose from. |
| `key` | `str` | Optional | The value to provide in the result. |
| `optional` | `bool` | Optional | True if this input is optional to provide. |
| `mtype` | `str` | Optional | The type of the required input. |
| `value` | `str` | Optional | The value can be pre-filled, if available. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.network_token_requestor import NetworkTokenRequestor
from adyen.models.sub_input_detail import SubInputDetail

sub_input_detail = SubInputDetail(
    configuration={
        'key0': 'configuration6',
        'key1': 'configuration7'
    },
    items=[
        NetworkTokenRequestor(
            id='id8',
            name='name8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    key='key0',
    optional=False,
    mtype='type0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

