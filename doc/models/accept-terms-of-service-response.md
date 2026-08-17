
# Accept Terms of Service Response

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
| `mtype` | [`Type64Enum`](../../doc/models/type-64-enum.md) | Optional | The type of Terms of Service.<br><br>Possible values:<br><br>* **adyenForPlatformsManage**<br>* **adyenIssuing**<br>* **adyenForPlatformsAdvanced**<br>* **adyenCapital**<br>* **adyenAccount**<br>* **adyenCard**<br>* **adyenFranchisee**<br>* **adyenPccr**<br>* **adyenChargeCard**<br>* **kycOnInvite** |

## Example

```python
from adyen.models.accept_terms_of_service_response import AcceptTermsOfServiceResponse

accept_terms_of_service_response = AcceptTermsOfServiceResponse(
    accepted_by='acceptedBy2',
    id='id4',
    ip_address='ipAddress4',
    language='language6',
    terms_of_service_document_id='termsOfServiceDocumentId2'
)
```

