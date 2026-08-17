
# Get Uploaded Documents Response

## Structure

`GetUploadedDocumentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_details` | [`List[DocumentDetail]`](../../doc/models/document-detail.md) | Optional | A list of the documents and their details. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |

## Example

```python
from adyen.models.document_detail import DocumentDetail
from adyen.models.document_type_enum import DocumentTypeEnum
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType
from adyen.models.get_uploaded_documents_response import GetUploadedDocumentsResponse

get_uploaded_documents_response = GetUploadedDocumentsResponse(
    document_details=[
        DocumentDetail(
            document_type=DocumentTypeEnum.COMPANY_REGISTRATION_SCREENING,
            account_holder_code='accountHolderCode0',
            bank_account_uuid='bankAccountUUID0',
            description='description4',
            filename='filename6',
            legal_arrangement_code='legalArrangementCode6'
        ),
        DocumentDetail(
            document_type=DocumentTypeEnum.COMPANY_REGISTRATION_SCREENING,
            account_holder_code='accountHolderCode0',
            bank_account_uuid='bankAccountUUID0',
            description='description4',
            filename='filename6',
            legal_arrangement_code='legalArrangementCode6'
        ),
        DocumentDetail(
            document_type=DocumentTypeEnum.COMPANY_REGISTRATION_SCREENING,
            account_holder_code='accountHolderCode0',
            bank_account_uuid='bankAccountUUID0',
            description='description4',
            filename='filename6',
            legal_arrangement_code='legalArrangementCode6'
        )
    ],
    invalid_fields=[
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        ),
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        ),
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        )
    ],
    psp_reference='pspReference4',
    result_code='resultCode0'
)
```

