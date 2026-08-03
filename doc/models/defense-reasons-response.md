
# Defense Reasons Response

*This model accepts additional fields of type Any.*

## Structure

`DefenseReasonsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `defense_reasons` | [`List[DefenseReason]`](../../doc/models/defense-reason.md) | Optional | The defense reasons that can be used to defend the dispute. |
| `dispute_service_result` | [`DisputeServiceResult`](../../doc/models/dispute-service-result.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.defense_document_type import DefenseDocumentType
from adyen.models.defense_reason import DefenseReason
from adyen.models.defense_reasons_response import DefenseReasonsResponse
from adyen.models.dispute_service_result import DisputeServiceResult

defense_reasons_response = DefenseReasonsResponse(
    dispute_service_result=DisputeServiceResult(
        success=False,
        error_message='errorMessage8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    defense_reasons=[
        DefenseReason(
            defense_reason_code='defenseReasonCode0',
            satisfied=False,
            defense_document_types=[
                DefenseDocumentType(
                    available=False,
                    defense_document_type_code='defenseDocumentTypeCode0',
                    requirement_level='requirementLevel4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                DefenseDocumentType(
                    available=False,
                    defense_document_type_code='defenseDocumentTypeCode0',
                    requirement_level='requirementLevel4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

