
# Document Detail 1

Details of the document being submitted.

*This model accepts additional fields of type Any.*

## Structure

`DocumentDetail1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Optional | The code of account holder, to which the document applies. |
| `bank_account_uuid` | `str` | Optional | The Adyen-generated [`bankAccountUUID`](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-bankAccountDetails-bankAccountUUID) to which the document must be linked. Refer to [Bank account check](https://docs.adyen.com/classic-platforms/verification-checks/bank-account-check#uploading-a-bank-statement) for details on when a document should be submitted.<br><br>> Required if the `documentType` is **BANK_STATEMENT**, where a document is being submitted in order to verify a bank account. |
| `description` | `str` | Optional | Description of the document. |
| `document_type` | [`DocumentType`](../../doc/models/document-type.md) | Required | - |
| `filename` | `str` | Optional | Filename of the document. |
| `legal_arrangement_code` | `str` | Optional | The Adyen-generated [`legalArrangementCode`](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-legalArrangements-legalArrangementCode) to which the document must be linked. |
| `legal_arrangement_entity_code` | `str` | Optional | The Adyen-generated [`legalArrangementEntityCode`](https://docs.adyen.com/api-explorer/#/Account/v6/post/createAccountHolder__resParam_accountHolderDetails-legalArrangements-legalArrangementEntities-legalArrangementEntityCode)  to which the document must be linked. |
| `shareholder_code` | `str` | Optional | The Adyen-generated [`shareholderCode`](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-businessDetails-shareholders-shareholderCode) to which the document must be linked. Refer to [Verification checks](https://docs.adyen.com/classic-platforms/verification-checks) for details on when a document should be submitted.<br><br>> Required if the account holder has a `legalEntity` of type **Business** and the `documentType` is either **PASSPORT**, **ID_CARD_FRONT**, **ID_CARD_BACK**, **DRIVING_LICENCE_FRONT**, or **DRIVING_LICENCE_BACK**. |
| `signatory_code` | `str` | Optional | The Adyen-generated [`signatoryCode`](https://docs.adyen.com/api-explorer/#/Account/v6/post/createAccountHolder__resParam_accountHolderDetails-businessDetails-signatories-signatoryCode) to which the document must be linked. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.document_detail_1 import DocumentDetail1
from adyen.models.document_type import DocumentType

document_detail_1 = DocumentDetail1(
    document_type=DocumentType.BANK_STATEMENT,
    account_holder_code='accountHolderCode0',
    bank_account_uuid='bankAccountUUID0',
    description='description4',
    filename='filename6',
    legal_arrangement_code='legalArrangementCode6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

