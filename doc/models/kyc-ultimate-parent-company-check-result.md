
# Kyc Ultimate Parent Company Check Result

*This model accepts additional fields of type Any.*

## Structure

`KycUltimateParentCompanyCheckResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checks` | [`List[KycCheckStatusData]`](../../doc/models/kyc-check-status-data.md) | Optional | A list of the checks and their statuses. |
| `ultimate_parent_company_code` | `str` | Optional | The code of the Ultimate Parent Company to which the check applies. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.kyc_check_status_data import KycCheckStatusData
from adyen.models.kyc_check_summary import KycCheckSummary
from adyen.models.kyc_ultimate_parent_company_check_result import KycUltimateParentCompanyCheckResult
from adyen.models.status_3 import Status3
from adyen.models.type_2 import Type2

kyc_ultimate_parent_company_check_result = KycUltimateParentCompanyCheckResult(
    checks=[
        KycCheckStatusData(
            status=Status3.INVALID_DATA,
            mtype=Type2.PASSPORT_VERIFICATION,
            required_fields=[
                'requiredFields0',
                'requiredFields1'
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
        ),
        KycCheckStatusData(
            status=Status3.INVALID_DATA,
            mtype=Type2.PASSPORT_VERIFICATION,
            required_fields=[
                'requiredFields0',
                'requiredFields1'
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
        ),
        KycCheckStatusData(
            status=Status3.INVALID_DATA,
            mtype=Type2.PASSPORT_VERIFICATION,
            required_fields=[
                'requiredFields0',
                'requiredFields1'
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
    ],
    ultimate_parent_company_code='ultimateParentCompanyCode2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

