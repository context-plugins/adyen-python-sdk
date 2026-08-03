
# Network Reason 2

Contains information that explains why the transfer was rejected or returned by the network.

*This model accepts additional fields of type Any.*

## Structure

`NetworkReason2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The reason code provided by the network. |
| `description` | `str` | Optional | The description of the reason code. |
| `namespace` | [`Namespace`](../../doc/models/namespace.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.namespace import Namespace
from adyen.models.network_reason_2 import NetworkReason2

network_reason_2 = NetworkReason2(
    code='code2',
    description='description6',
    namespace=Namespace.ISO8583RESPONSECODE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

