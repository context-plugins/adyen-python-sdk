
# Delete Defense Document Request

*This model accepts additional fields of type Any.*

## Structure

`DeleteDefenseDocumentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `defense_document_type` | `str` | Required | The document type code of the defense document. |
| `dispute_psp_reference` | `str` | Required | The PSP reference assigned to the dispute. |
| `merchant_account_code` | `str` | Required | The merchant account identifier, for which you want to process the dispute transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.delete_defense_document_request import DeleteDefenseDocumentRequest

delete_defense_document_request = DeleteDefenseDocumentRequest(
    defense_document_type='defenseDocumentType8',
    dispute_psp_reference='disputePspReference0',
    merchant_account_code='merchantAccountCode2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

