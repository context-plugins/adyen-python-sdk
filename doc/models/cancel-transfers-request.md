
# Cancel Transfers Request

*This model accepts additional fields of type Any.*

## Structure

`CancelTransfersRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_ids` | `List[str]` | Optional | Contains the unique identifiers of the transfers that you want to cancel. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.cancel_transfers_request import CancelTransfersRequest

cancel_transfers_request = CancelTransfersRequest(
    transfer_ids=[
        'transferIds2',
        'transferIds3'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

