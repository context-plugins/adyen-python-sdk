
# Document

*This model accepts additional fields of type Any.*

## Structure

`Document`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attachment` | [`Attachment`](../../doc/models/attachment.md) | Optional | - |
| `attachments` | [`List[Attachment]`](../../doc/models/attachment.md) | Optional | Array that contains the document. The array supports multiple attachments for uploading different sides or pages of a document. |
| `creation_date` | `datetime` | Optional, Read-only | The creation date of the document. |
| `description` | `str` | Required | Your description for the document. |
| `expiry_date` | `str` | Optional | The expiry date of the document, in YYYY-MM-DD format. |
| `file_name` | `str` | Optional | The filename of the document. |
| `id` | `str` | Optional, Read-only | The unique identifier of the document. |
| `issuer_country` | `str` | Optional | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the document was issued. For example, **US**. |
| `issuer_state` | `str` | Optional | The state or province where the document was issued (AU only). |
| `modification_date` | `datetime` | Optional, Read-only | The modification date of the document. |
| `number` | `str` | Optional | The number in the document. |
| `owner` | [`OwnerEntity`](../../doc/models/owner-entity.md) | Optional | - |
| `mtype` | [`Type81`](../../doc/models/type-81.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.attachment import Attachment
from adyen.models.document import Document
from adyen.models.type_81 import Type81

document = Document(
    description='description6',
    mtype=Type81.PASSPORT,
    attachment=Attachment(
        content='content2',
        content_type='contentType4',
        filename='filename0',
        page_name='pageName0',
        page_type='pageType6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    attachments=[
        Attachment(
            content='content4',
            content_type='contentType6',
            filename='filename2',
            page_name='pageName2',
            page_type='pageType8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Attachment(
            content='content4',
            content_type='contentType6',
            filename='filename2',
            page_name='pageName2',
            page_type='pageType8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Attachment(
            content='content4',
            content_type='contentType6',
            filename='filename2',
            page_name='pageName2',
            page_type='pageType8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    expiry_date='expiryDate4',
    file_name='fileName0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

