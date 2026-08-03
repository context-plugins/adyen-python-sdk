
# Get Uploaded Documents Request

*This model accepts additional fields of type Any.*

## Structure

`GetUploadedDocumentsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the Account Holder for which to retrieve the documents. |
| `bank_account_uuid` | `str` | Optional | The code of the Bank Account for which to retrieve the documents. |
| `shareholder_code` | `str` | Optional | The code of the Shareholder for which to retrieve the documents. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.get_uploaded_documents_request import GetUploadedDocumentsRequest

get_uploaded_documents_request = GetUploadedDocumentsRequest(
    account_holder_code='accountHolderCode2',
    bank_account_uuid='bankAccountUUID2',
    shareholder_code='shareholderCode4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

