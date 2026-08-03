
# Defense Document Type

*This model accepts additional fields of type Any.*

## Structure

`DefenseDocumentType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `available` | `bool` | Required | When **true**, you've successfully uploaded this type of defense document. When **false**, you haven't uploaded this defense document type. |
| `defense_document_type_code` | `str` | Required | The document type code of the defense document. |
| `requirement_level` | `str` | Required | Indicates to what extent the defense document is required in the defense process.<br><br>Possible values:<br><br>* **Required**: You must supply the document.<br><br>* **OneOrMore**: You must supply at least one of the documents with this label.<br><br>* **Optional**: You can choose to supply the document.<br><br>* **AlternativeRequired**: You must supply a generic defense document. To enable this functionality, contact our Support Team. When enabled, you can supply a generic defense document for all schemes. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.defense_document_type import DefenseDocumentType

defense_document_type = DefenseDocumentType(
    available=False,
    defense_document_type_code='defenseDocumentTypeCode2',
    requirement_level='requirementLevel8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

