
# Defense Reason

*This model accepts additional fields of type Any.*

## Structure

`DefenseReason`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `defense_document_types` | [`List[DefenseDocumentType]`](../../doc/models/defense-document-type.md) | Optional | Array of defense document types for a specific defense reason. Indicates the document types that you can submit to the schemes to defend this dispute, and whether they are required. |
| `defense_reason_code` | `str` | Required | The defense reason code that was selected to defend this dispute. |
| `satisfied` | `bool` | Required | Indicates if sufficient defense material has been supplied. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.defense_document_type import DefenseDocumentType
from adyen.models.defense_reason import DefenseReason

defense_reason = DefenseReason(
    defense_reason_code='defenseReasonCode8',
    satisfied=False,
    defense_document_types=[
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
```

