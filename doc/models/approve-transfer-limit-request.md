
# Approve Transfer Limit Request

*This model accepts additional fields of type Any.*

## Structure

`ApproveTransferLimitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_limit_ids` | `List[str]` | Required | A list that includes the `transferLimitId` of all the pending transfer limits you want to approve.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `2147483647` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.approve_transfer_limit_request import ApproveTransferLimitRequest

approve_transfer_limit_request = ApproveTransferLimitRequest(
    transfer_limit_ids=[
        'transferLimitIds6'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

