
# Defense Document

## Structure

`DefenseDocument`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Required | The content of the defense document. |
| `content_type` | `str` | Required | The content type of the defense document. |
| `defense_document_type_code` | `str` | Required | The document type code of the defense document. |

## Example

```python
from adyen.models.defense_document import DefenseDocument

defense_document = DefenseDocument(
    content='content0',
    content_type='contentType2',
    defense_document_type_code='defenseDocumentTypeCode6'
)
```

