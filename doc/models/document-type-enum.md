
# Document Type Enum

The type of the document. Refer to [Verification checks](https://docs.adyen.com/classic-platforms/verification-checks) for details on when each document type should be submitted and for the accepted file formats.

Permitted values:

* **BANK_STATEMENT**: A file containing a bank statement or other document proving ownership of a specific bank account.
* **COMPANY_REGISTRATION_SCREENING** (Supported from v5 and later): A file containing a company registration document.
* **CONSTITUTIONAL_DOCUMENT**: A file containing information about the account holder's legal arrangement.
* **PASSPORT**: A file containing the identity page(s) of a passport.
* **ID_CARD_FRONT**: A file containing only the front of the ID card. In order for a document to be usable, both the **ID_CARD_FRONT** and **ID_CARD_BACK** must be submitted.
* **ID_CARD_BACK**: A file containing only the back of the ID card. In order for a document to be usable, both the **ID_CARD_FRONT** and **ID_CARD_BACK** must be submitted.
* **DRIVING_LICENCE_FRONT**: A file containing only the front of the driving licence. In order for a document to be usable, both the **DRIVING_LICENCE_FRONT** and **DRIVING_LICENCE_BACK** must be submitted.
* **DRIVING_LICENCE_BACK**: A file containing only the back of the driving licence. In order for a document to be usable, both the **DRIVING_LICENCE_FRONT** and **DRIVING_LICENCE_FRONT** must be submitted.

## Enumeration

`DocumentTypeEnum`

## Fields

| Name |
|  --- |
| `BANK_STATEMENT` |
| `BSN` |
| `COMPANY_REGISTRATION_SCREENING` |
| `CONSTITUTIONAL_DOCUMENT` |
| `DRIVING_LICENCE` |
| `DRIVING_LICENCE_BACK` |
| `DRIVING_LICENCE_FRONT` |
| `ID_CARD` |
| `ID_CARD_BACK` |
| `ID_CARD_FRONT` |
| `PASSPORT` |
| `PROOF_OF_RESIDENCY` |
| `SSN` |
| `SUPPORTING_DOCUMENTS` |

## Example

```python
from adyen.models.document_type_enum import DocumentTypeEnum

document_type = DocumentTypeEnum.PASSPORT
```

