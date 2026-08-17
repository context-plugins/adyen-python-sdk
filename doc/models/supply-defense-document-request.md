
# Supply Defense Document Request

## Structure

`SupplyDefenseDocumentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `defense_documents` | [`List[DefenseDocument]`](../../doc/models/defense-document.md) | Required | An array containing a list of the defense documents. |
| `dispute_psp_reference` | `str` | Required | The PSP reference assigned to the dispute. |
| `merchant_account_code` | `str` | Required | The merchant account identifier, for which you want to process the dispute transaction. |

## Example

```python
from adyen.models.defense_document import DefenseDocument
from adyen.models.supply_defense_document_request import SupplyDefenseDocumentRequest

supply_defense_document_request = SupplyDefenseDocumentRequest(
    defense_documents=[
        DefenseDocument(
            content='content0',
            content_type='contentType2',
            defense_document_type_code='defenseDocumentTypeCode6'
        )
    ],
    dispute_psp_reference='disputePspReference4',
    merchant_account_code='merchantAccountCode6'
)
```

