
# Kyc Legal Arrangement Entity Check Result

*This model accepts additional fields of type Any.*

## Structure

`KycLegalArrangementEntityCheckResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checks` | [`List[KycCheckStatusData]`](../../doc/models/kyc-check-status-data.md) | Optional | A list of the checks and their statuses. |
| `legal_arrangement_code` | `str` | Optional | The unique ID of the legal arrangement to which the entity belongs. |
| `legal_arrangement_entity_code` | `str` | Optional | The unique ID of the legal arrangement entity to which the check applies. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.kyc_check_status_data import KycCheckStatusData
from adyen.models.kyc_check_summary import KycCheckSummary
from adyen.models.kyc_legal_arrangement_entity_check_result import KycLegalArrangementEntityCheckResult
from adyen.models.status_3 import Status3
from adyen.models.type_2 import Type2

kyc_legal_arrangement_entity_check_result = KycLegalArrangementEntityCheckResult(
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
        )
    ],
    legal_arrangement_code='legalArrangementCode6',
    legal_arrangement_entity_code='legalArrangementEntityCode8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

