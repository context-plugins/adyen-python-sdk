
# Kyc Check Status Data

*This model accepts additional fields of type Any.*

## Structure

`KycCheckStatusData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `required_fields` | `List[str]` | Optional | A list of the fields required for execution of the check. |
| `status` | [`Status3`](../../doc/models/status-3.md) | Required | - |
| `summary` | [`KycCheckSummary`](../../doc/models/kyc-check-summary.md) | Optional | - |
| `mtype` | [`Type2`](../../doc/models/type-2.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.kyc_check_status_data import KycCheckStatusData
from adyen.models.kyc_check_summary import KycCheckSummary
from adyen.models.status_3 import Status3
from adyen.models.type_2 import Type2

kyc_check_status_data = KycCheckStatusData(
    status=Status3.PENDING,
    mtype=Type2.PAYOUT_METHOD_VERIFICATION,
    required_fields=[
        'requiredFields8',
        'requiredFields7',
        'requiredFields6'
    ],
    summary=KycCheckSummary(
        kyc_check_code=128,
        kyc_check_description='kycCheckDescription8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

