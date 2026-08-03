
# Get Terms of Service Document Request

*This model accepts additional fields of type Any.*

## Structure

`GetTermsOfServiceDocumentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `language` | `str` | Required | The language to be used for the Terms of Service document, specified by the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code. Possible values: **en** for English or **fr** for French. |
| `terms_of_service_document_format` | `str` | Optional | The requested format for the Terms of Service document. Default value: JSON. Possible values: **JSON**, **PDF**, or **TXT**. |
| `mtype` | [`Type25`](../../doc/models/type-25.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.get_terms_of_service_document_request import GetTermsOfServiceDocumentRequest
from adyen.models.type_25 import Type25

get_terms_of_service_document_request = GetTermsOfServiceDocumentRequest(
    language='language4',
    mtype=Type25.ADYENPCCR,
    terms_of_service_document_format='termsOfServiceDocumentFormat6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

