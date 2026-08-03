
# Accept Terms of Service Response

*This model accepts additional fields of type Any.*

## Structure

`AcceptTermsOfServiceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accepted_by` | `str` | Optional | The unique identifier of the user that accepted the Terms of Service. |
| `id` | `str` | Optional | The unique identifier of the Terms of Service acceptance. |
| `ip_address` | `str` | Optional | The IP address of the user that accepted the Terms of Service. |
| `language` | `str` | Optional | The language used for the Terms of Service document, specified by the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code. Possible value: **en** for English or **fr** for French.<br><br>Note that French is only available for some integration types in certain countries/regions. Reach out to your Adyen contact for more information. |
| `terms_of_service_document_id` | `str` | Optional | The unique identifier of the Terms of Service document. |
| `mtype` | [`Type25`](../../doc/models/type-25.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.accept_terms_of_service_response import AcceptTermsOfServiceResponse

accept_terms_of_service_response = AcceptTermsOfServiceResponse(
    accepted_by='acceptedBy2',
    id='id4',
    ip_address='ipAddress4',
    language='language6',
    terms_of_service_document_id='termsOfServiceDocumentId2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

