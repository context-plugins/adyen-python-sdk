
# Defense Reasons Response

## Structure

`DefenseReasonsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `defense_reasons` | [`List[DefenseReason]`](../../doc/models/defense-reason.md) | Optional | The defense reasons that can be used to defend the dispute. |
| `dispute_service_result` | [`DisputeServiceResult1`](../../doc/models/dispute-service-result-1.md) | Required | The result of the dispute service. |

## Example

```python
from adyen.models.defense_document_type import DefenseDocumentType
from adyen.models.defense_reason import DefenseReason
from adyen.models.defense_reasons_response import DefenseReasonsResponse
from adyen.models.dispute_service_result_1 import DisputeServiceResult1

defense_reasons_response = DefenseReasonsResponse(
    dispute_service_result=DisputeServiceResult1(
        success=False,
        error_message='errorMessage8'
    ),
    defense_reasons=[
        DefenseReason(
            defense_reason_code='defenseReasonCode0',
            satisfied=False,
            defense_document_types=[
                DefenseDocumentType(
                    available=False,
                    defense_document_type_code='defenseDocumentTypeCode0',
                    requirement_level='requirementLevel4'
                ),
                DefenseDocumentType(
                    available=False,
                    defense_document_type_code='defenseDocumentTypeCode0',
                    requirement_level='requirementLevel4'
                )
            ]
        )
    ]
)
```

