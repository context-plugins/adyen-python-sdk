
# Document Reference

## Structure

`DocumentReference`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | `bool` | Optional | Identifies whether the document is active and used for checks. |
| `description` | `str` | Optional | Your description for the document. |
| `file_name` | `str` | Optional | Document name. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `modification_date` | `datetime` | Optional | The modification date of the document. |
| `pages` | [`List[DocumentPage]`](../../doc/models/document-page.md) | Optional | List of document pages |
| `mtype` | `str` | Optional | Type of document, used when providing an ID number or uploading a document. |

## Example

```python
import dateutil.parser

from adyen.models.document_reference import DocumentReference

document_reference = DocumentReference(
    active=False,
    description='description6',
    file_name='fileName0',
    id='id6',
    modification_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

