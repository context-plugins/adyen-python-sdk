
# Delete Legal Arrangement Request

## Structure

`DeleteLegalArrangementRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder. |
| `legal_arrangements` | [`List[LegalArrangementRequest]`](../../doc/models/legal-arrangement-request.md) | Required | List of legal arrangements. |

## Example

```python
from adyen.models.delete_legal_arrangement_request import DeleteLegalArrangementRequest
from adyen.models.legal_arrangement_request import LegalArrangementRequest

delete_legal_arrangement_request = DeleteLegalArrangementRequest(
    account_holder_code='accountHolderCode2',
    legal_arrangements=[
        LegalArrangementRequest(
            legal_arrangement_code='legalArrangementCode2',
            legal_arrangement_entity_codes=[
                'legalArrangementEntityCodes8'
            ]
        )
    ]
)
```

