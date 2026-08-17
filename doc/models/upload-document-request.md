
# Upload Document Request

## Structure

`UploadDocumentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_content` | `str` | Required | The content of the document, in Base64-encoded string format.<br><br>To learn about document requirements, refer to [Verification checks](https://docs.adyen.com/classic-platforms/verification-checks). |
| `document_detail` | [`DocumentDetail1`](../../doc/models/document-detail-1.md) | Required | Details of the document being submitted. |

## Example

```python
from adyen.models.document_detail_1 import DocumentDetail1
from adyen.models.document_type_enum import DocumentTypeEnum
from adyen.models.upload_document_request import UploadDocumentRequest

upload_document_request = UploadDocumentRequest(
    document_content='documentContent6',
    document_detail=DocumentDetail1(
        document_type=DocumentTypeEnum.SSN,
        account_holder_code='accountHolderCode0',
        bank_account_uuid='bankAccountUUID0',
        description='description6',
        filename='filename6',
        legal_arrangement_code='legalArrangementCode6'
    )
)
```

