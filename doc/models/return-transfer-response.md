
# Return Transfer Response

*This model accepts additional fields of type Any.*

## Structure

`ReturnTransferResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the return. |
| `reference` | `str` | Optional | Your internal reference for the return. |
| `status` | [`Status61`](../../doc/models/status-61.md) | Optional | - |
| `transfer_id` | `str` | Optional | The unique identifier of the original transfer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.return_transfer_response import ReturnTransferResponse
from adyen.models.status_61 import Status61

return_transfer_response = ReturnTransferResponse(
    id='id8',
    reference='reference4',
    status=Status61.AUTHORISED,
    transfer_id='transferId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

