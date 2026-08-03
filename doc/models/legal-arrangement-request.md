
# Legal Arrangement Request

*This model accepts additional fields of type Any.*

## Structure

`LegalArrangementRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `legal_arrangement_code` | `str` | Required | The code of the legal arrangement to be deleted. If you also send `legalArrangementEntityCodes`, only the entities listed will be deleted. |
| `legal_arrangement_entity_codes` | `List[str]` | Optional | List of legal arrangement entities to be deleted. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.legal_arrangement_request import LegalArrangementRequest

legal_arrangement_request = LegalArrangementRequest(
    legal_arrangement_code='legalArrangementCode8',
    legal_arrangement_entity_codes=[
        'legalArrangementEntityCodes4'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

