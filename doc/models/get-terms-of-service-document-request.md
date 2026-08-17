
# Get Terms of Service Document Request

## Structure

`GetTermsOfServiceDocumentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `language` | `str` | Required | The language to be used for the Terms of Service document, specified by the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code. Possible values: **en** for English or **fr** for French. |
| `terms_of_service_document_format` | `str` | Optional | The requested format for the Terms of Service document. Default value: JSON. Possible values: **JSON**, **PDF**, or **TXT**. |
| `mtype` | [`Type64Enum`](../../doc/models/type-64-enum.md) | Required | The type of Terms of Service.<br><br>Possible values:<br><br>* **adyenForPlatformsManage**<br>* **adyenIssuing**<br>* **adyenForPlatformsAdvanced**<br>* **adyenCapital**<br>* **adyenAccount**<br>* **adyenCard**<br>* **adyenFranchisee**<br>* **adyenPccr**<br>* **adyenChargeCard**<br>* **kycOnInvite** |

## Example

```python
from adyen.models.get_terms_of_service_document_request import GetTermsOfServiceDocumentRequest
from adyen.models.type_64_enum import Type64Enum

get_terms_of_service_document_request = GetTermsOfServiceDocumentRequest(
    language='language4',
    mtype=Type64Enum.ADYENPCCR,
    terms_of_service_document_format='termsOfServiceDocumentFormat6'
)
```

