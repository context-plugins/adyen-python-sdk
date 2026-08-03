
# Network Reason

*This model accepts additional fields of type Any.*

## Structure

`NetworkReason`

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
from adyen.models.network_reason import NetworkReason

network_reason = NetworkReason(
    code='code8',
    description='description0',
    namespace=Namespace.UKFPSRETURNREASONCODE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

