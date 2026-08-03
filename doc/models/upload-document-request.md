
# Upload Document Request

*This model accepts additional fields of type Any.*

## Structure

`UploadDocumentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_content` | `str` | Required | The content of the document, in Base64-encoded string format.<br><br>To learn about document requirements, refer to [Verification checks](https://docs.adyen.com/classic-platforms/verification-checks). |
| `document_detail` | [`DocumentDetail`](../../doc/models/document-detail.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.document_detail import DocumentDetail
from adyen.models.document_type import DocumentType
from adyen.models.upload_document_request import UploadDocumentRequest

upload_document_request = UploadDocumentRequest(
    document_content='documentContent6',
    document_detail=DocumentDetail(
        document_type=DocumentType.SSN,
        account_holder_code='accountHolderCode0',
        bank_account_uuid='bankAccountUUID0',
        description='description6',
        filename='filename6',
        legal_arrangement_code='legalArrangementCode6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

