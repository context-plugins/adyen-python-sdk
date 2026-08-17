
# Approve Transfer Limit Request

## Structure

`ApproveTransferLimitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_limit_ids` | `List[str]` | Required | A list that includes the `transferLimitId` of all the pending transfer limits you want to approve.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2147483647` |

## Example

```python
from adyen.models.approve_transfer_limit_request import ApproveTransferLimitRequest

approve_transfer_limit_request = ApproveTransferLimitRequest(
    transfer_limit_ids=[
        'transferLimitIds6'
    ]
)
```

