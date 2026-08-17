
# Get Uploaded Documents Request

## Structure

`GetUploadedDocumentsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the Account Holder for which to retrieve the documents. |
| `bank_account_uuid` | `str` | Optional | The code of the Bank Account for which to retrieve the documents. |
| `shareholder_code` | `str` | Optional | The code of the Shareholder for which to retrieve the documents. |

## Example

```python
from adyen.models.get_uploaded_documents_request import GetUploadedDocumentsRequest

get_uploaded_documents_request = GetUploadedDocumentsRequest(
    account_holder_code='accountHolderCode2',
    bank_account_uuid='bankAccountUUID2',
    shareholder_code='shareholderCode4'
)
```

