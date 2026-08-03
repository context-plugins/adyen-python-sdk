
# Defense Document

*This model accepts additional fields of type Any.*

## Structure

`DefenseDocument`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Required | The content of the defense document. |
| `content_type` | `str` | Required | The content type of the defense document. |
| `defense_document_type_code` | `str` | Required | The document type code of the defense document. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.defense_document import DefenseDocument

defense_document = DefenseDocument(
    content='content0',
    content_type='contentType2',
    defense_document_type_code='defenseDocumentTypeCode6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

