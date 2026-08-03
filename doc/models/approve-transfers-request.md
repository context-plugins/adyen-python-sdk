
# Approve Transfers Request

*This model accepts additional fields of type Any.*

## Structure

`ApproveTransfersRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_ids` | `List[str]` | Optional | Contains the unique identifiers of the transfers that you want to approve. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.approve_transfers_request import ApproveTransfersRequest

approve_transfers_request = ApproveTransfersRequest(
    transfer_ids=[
        'transferIds4',
        'transferIds3'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

