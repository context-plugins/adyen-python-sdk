
# Transfer Review 1

Contains status updates related to additional reviews.

*This model accepts additional fields of type Any.*

## Structure

`TransferReview1`

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
from adyen.models.transfer_review_1 import TransferReview1

transfer_review_1 = TransferReview1(
    number_of_approvals_required=250,
    sca_on_approval=ScaOnApproval.NOTAPPLICABLE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

