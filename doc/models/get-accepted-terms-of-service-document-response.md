
# Get Accepted Terms of Service Document Response

## Structure

`GetAcceptedTermsOfServiceDocumentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document` | `str` | Optional | The accepted Terms of Service document in the requested format represented as a Base64-encoded bytes array. |
| `id` | `str` | Optional | The unique identifier of the legal entity. |
| `terms_of_service_acceptance_reference` | `str` | Optional | An Adyen-generated reference for the accepted Terms of Service. |
| `terms_of_service_document_format` | [`TermsOfServiceDocumentFormatEnum`](../../doc/models/terms-of-service-document-format-enum.md) | Optional | The format of the Terms of Service document. |

## Example

```python
from adyen.models.get_accepted_terms_of_service_document_response import GetAcceptedTermsOfServiceDocumentResponse
from adyen.models.terms_of_service_document_format_enum import TermsOfServiceDocumentFormatEnum

get_accepted_terms_of_service_document_response = GetAcceptedTermsOfServiceDocumentResponse(
    document='document0',
    id='id6',
    terms_of_service_acceptance_reference='termsOfServiceAcceptanceReference6',
    terms_of_service_document_format=TermsOfServiceDocumentFormatEnum.PDF
)
```

