
# Update Network Token Request

*This model accepts additional fields of type Any.*

## Structure

`UpdateNetworkTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status16`](../../doc/models/status-16.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.status_16 import Status16
from adyen.models.update_network_token_request import UpdateNetworkTokenRequest

update_network_token_request = UpdateNetworkTokenRequest(
    status=Status16.CLOSED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

