
# Get Terms of Service Document Response

*This model accepts additional fields of type Any.*

## Structure

`GetTermsOfServiceDocumentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document` | `str` | Optional | The Terms of Service document in Base64-encoded format. |
| `id` | `str` | Optional | The unique identifier of the legal entity. |
| `language` | `str` | Optional | The language used for the Terms of Service document, specified by the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code. Possible value: **en** for English or **fr** for French.<br><br>Note that French is only available for some integration types in certain countries/regions. Reach out to your Adyen contact for more information. |
| `terms_of_service_document_format` | `str` | Optional | The format of the Terms of Service document. |
| `terms_of_service_document_id` | `str` | Optional | The unique identifier of the Terms of Service document. |
| `mtype` | [`Type25`](../../doc/models/type-25.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.get_terms_of_service_document_response import GetTermsOfServiceDocumentResponse

get_terms_of_service_document_response = GetTermsOfServiceDocumentResponse(
    document='document8',
    id='id4',
    language='language6',
    terms_of_service_document_format='termsOfServiceDocumentFormat8',
    terms_of_service_document_id='termsOfServiceDocumentId8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

