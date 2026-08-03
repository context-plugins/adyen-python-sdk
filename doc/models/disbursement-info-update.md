
# Disbursement Info Update

*This model accepts additional fields of type Any.*

## Structure

`DisbursementInfoUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `repayment` | [`DisbursementRepaymentInfoUpdate`](../../doc/models/disbursement-repayment-info-update.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.disbursement_info_update import DisbursementInfoUpdate
from adyen.models.disbursement_repayment_info_update import DisbursementRepaymentInfoUpdate

disbursement_info_update = DisbursementInfoUpdate(
    repayment=DisbursementRepaymentInfoUpdate(
        basis_points=18,
        update_description='updateDescription0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

