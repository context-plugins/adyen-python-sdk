
# Transfer Review 1

Contains status updates related to additional reviews.

## Structure

`TransferReview1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number_of_approvals_required` | `int` | Optional | Shows the number of [approvals](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/approve) required to process the transfer. |
| `sca_on_approval` | [`ScaOnApprovalEnum`](../../doc/models/sca-on-approval-enum.md) | Optional | Shows the status of the Strong Customer Authentication (SCA) process.<br><br>Possible values: **required**, **notApplicable**. |

## Example

```python
from adyen.models.sca_on_approval_enum import ScaOnApprovalEnum
from adyen.models.transfer_review_1 import TransferReview1

transfer_review_1 = TransferReview1(
    number_of_approvals_required=250,
    sca_on_approval=ScaOnApprovalEnum.NOTAPPLICABLE
)
```

