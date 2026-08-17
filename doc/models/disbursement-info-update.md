
# Disbursement Info Update

## Structure

`DisbursementInfoUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `repayment` | [`DisbursementRepaymentInfoUpdate2`](../../doc/models/disbursement-repayment-info-update-2.md) | Optional | Contains information about the basis points configured for repaying the disbursement. |

## Example

```python
from adyen.models.disbursement_info_update import DisbursementInfoUpdate
from adyen.models.disbursement_repayment_info_update_2 import DisbursementRepaymentInfoUpdate2

disbursement_info_update = DisbursementInfoUpdate(
    repayment=DisbursementRepaymentInfoUpdate2(
        basis_points=18,
        update_description='updateDescription0'
    )
)
```

