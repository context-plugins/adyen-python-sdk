
# Get Accepted Terms of Service Document Response

*This model accepts additional fields of type Any.*

## Structure

`GetAcceptedTermsOfServiceDocumentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document` | `str` | Optional | The accepted Terms of Service document in the requested format represented as a Base64-encoded bytes array. |
| `id` | `str` | Optional | The unique identifier of the legal entity. |
| `terms_of_service_acceptance_reference` | `str` | Optional | An Adyen-generated reference for the accepted Terms of Service. |
| `terms_of_service_document_format` | [`TermsOfServiceDocumentFormat`](../../doc/models/terms-of-service-document-format.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.get_accepted_terms_of_service_document_response import GetAcceptedTermsOfServiceDocumentResponse
from adyen.models.terms_of_service_document_format import TermsOfServiceDocumentFormat

get_accepted_terms_of_service_document_response = GetAcceptedTermsOfServiceDocumentResponse(
    document='document0',
    id='id6',
    terms_of_service_acceptance_reference='termsOfServiceAcceptanceReference6',
    terms_of_service_document_format=TermsOfServiceDocumentFormat.PDF,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

