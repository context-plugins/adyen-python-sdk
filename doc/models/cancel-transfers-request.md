
# Cancel Transfers Request

## Structure

`CancelTransfersRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_ids` | `List[str]` | Optional | Contains the unique identifiers of the transfers that you want to cancel. |

## Example

```python
from adyen.models.cancel_transfers_request import CancelTransfersRequest

cancel_transfers_request = CancelTransfersRequest(
    transfer_ids=[
        'transferIds2',
        'transferIds3'
    ]
)
```

