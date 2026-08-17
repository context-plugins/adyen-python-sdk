
# Legal Arrangement Request

## Structure

`LegalArrangementRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `legal_arrangement_code` | `str` | Required | The code of the legal arrangement to be deleted. If you also send `legalArrangementEntityCodes`, only the entities listed will be deleted. |
| `legal_arrangement_entity_codes` | `List[str]` | Optional | List of legal arrangement entities to be deleted. |

## Example

```python
from adyen.models.legal_arrangement_request import LegalArrangementRequest

legal_arrangement_request = LegalArrangementRequest(
    legal_arrangement_code='legalArrangementCode8',
    legal_arrangement_entity_codes=[
        'legalArrangementEntityCodes4'
    ]
)
```

