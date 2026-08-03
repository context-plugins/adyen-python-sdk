
# Transfer Review

*This model accepts additional fields of type Any.*

## Structure

`TransferReview`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number_of_approvals_required` | `int` | Optional | Shows the number of [approvals](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/approve) required to process the transfer. |
| `sca_on_approval` | [`ScaOnApproval`](../../doc/models/sca-on-approval.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sca_on_approval import ScaOnApproval
from adyen.models.transfer_review import TransferReview

transfer_review = TransferReview(
    number_of_approvals_required=12,
    sca_on_approval=ScaOnApproval.COMPLETED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

