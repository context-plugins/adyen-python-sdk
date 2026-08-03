
# Delete Legal Arrangement Request

*This model accepts additional fields of type Any.*

## Structure

`DeleteLegalArrangementRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder. |
| `legal_arrangements` | [`List[LegalArrangementRequest]`](../../doc/models/legal-arrangement-request.md) | Required | List of legal arrangements. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.delete_legal_arrangement_request import DeleteLegalArrangementRequest
from adyen.models.legal_arrangement_request import LegalArrangementRequest

delete_legal_arrangement_request = DeleteLegalArrangementRequest(
    account_holder_code='accountHolderCode2',
    legal_arrangements=[
        LegalArrangementRequest(
            legal_arrangement_code='legalArrangementCode2',
            legal_arrangement_entity_codes=[
                'legalArrangementEntityCodes8'
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

