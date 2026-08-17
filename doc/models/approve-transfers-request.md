
# Approve Transfers Request

## Structure

`ApproveTransfersRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_ids` | `List[str]` | Optional | Contains the unique identifiers of the transfers that you want to approve. |

## Example

```python
from adyen.models.approve_transfers_request import ApproveTransfersRequest

approve_transfers_request = ApproveTransfersRequest(
    transfer_ids=[
        'transferIds4',
        'transferIds3'
    ]
)
```

