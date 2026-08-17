
# Document Detail 1

Details of the document being submitted.

## Structure

`DocumentDetail1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Optional | The code of account holder, to which the document applies. |
| `bank_account_uuid` | `str` | Optional | The Adyen-generated [`bankAccountUUID`](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-bankAccountDetails-bankAccountUUID) to which the document must be linked. Refer to [Bank account check](https://docs.adyen.com/classic-platforms/verification-checks/bank-account-check#uploading-a-bank-statement) for details on when a document should be submitted.<br><br>> Required if the `documentType` is **BANK_STATEMENT**, where a document is being submitted in order to verify a bank account. |
| `description` | `str` | Optional | Description of the document. |
| `document_type` | [`DocumentTypeEnum`](../../doc/models/document-type-enum.md) | Required | The type of the document. Refer to [Verification checks](https://docs.adyen.com/classic-platforms/verification-checks) for details on when each document type should be submitted and for the accepted file formats.<br><br>Permitted values:<br><br>* **BANK_STATEMENT**: A file containing a bank statement or other document proving ownership of a specific bank account.<br>* **COMPANY_REGISTRATION_SCREENING** (Supported from v5 and later): A file containing a company registration document.<br>* **CONSTITUTIONAL_DOCUMENT**: A file containing information about the account holder's legal arrangement.<br>* **PASSPORT**: A file containing the identity page(s) of a passport.<br>* **ID_CARD_FRONT**: A file containing only the front of the ID card. In order for a document to be usable, both the **ID_CARD_FRONT** and **ID_CARD_BACK** must be submitted.<br>* **ID_CARD_BACK**: A file containing only the back of the ID card. In order for a document to be usable, both the **ID_CARD_FRONT** and **ID_CARD_BACK** must be submitted.<br>* **DRIVING_LICENCE_FRONT**: A file containing only the front of the driving licence. In order for a document to be usable, both the **DRIVING_LICENCE_FRONT** and **DRIVING_LICENCE_BACK** must be submitted.<br>* **DRIVING_LICENCE_BACK**: A file containing only the back of the driving licence. In order for a document to be usable, both the **DRIVING_LICENCE_FRONT** and **DRIVING_LICENCE_FRONT** must be submitted. |
| `filename` | `str` | Optional | Filename of the document. |
| `legal_arrangement_code` | `str` | Optional | The Adyen-generated [`legalArrangementCode`](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-legalArrangements-legalArrangementCode) to which the document must be linked. |
| `legal_arrangement_entity_code` | `str` | Optional | The Adyen-generated [`legalArrangementEntityCode`](https://docs.adyen.com/api-explorer/#/Account/v6/post/createAccountHolder__resParam_accountHolderDetails-legalArrangements-legalArrangementEntities-legalArrangementEntityCode)  to which the document must be linked. |
| `shareholder_code` | `str` | Optional | The Adyen-generated [`shareholderCode`](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-businessDetails-shareholders-shareholderCode) to which the document must be linked. Refer to [Verification checks](https://docs.adyen.com/classic-platforms/verification-checks) for details on when a document should be submitted.<br><br>> Required if the account holder has a `legalEntity` of type **Business** and the `documentType` is either **PASSPORT**, **ID_CARD_FRONT**, **ID_CARD_BACK**, **DRIVING_LICENCE_FRONT**, or **DRIVING_LICENCE_BACK**. |
| `signatory_code` | `str` | Optional | The Adyen-generated [`signatoryCode`](https://docs.adyen.com/api-explorer/#/Account/v6/post/createAccountHolder__resParam_accountHolderDetails-businessDetails-signatories-signatoryCode) to which the document must be linked. |

## Example

```python
from adyen.models.document_detail_1 import DocumentDetail1
from adyen.models.document_type_enum import DocumentTypeEnum

document_detail_1 = DocumentDetail1(
    document_type=DocumentTypeEnum.BANK_STATEMENT,
    account_holder_code='accountHolderCode0',
    bank_account_uuid='bankAccountUUID0',
    description='description4',
    filename='filename6',
    legal_arrangement_code='legalArrangementCode6'
)
```

