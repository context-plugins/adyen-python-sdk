<!-- Generated file — do not edit; regenerated with the SDK. -->

# Verification — operations

Accessor: `client.verification` · Source: `adyen/apis/verification.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.verification.post_check_account_holder

- **Route**: `POST /checkAccountHolder`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_check_account_holder(*, body: PerformVerificationRequest | PerformVerificationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenericResponse`
- **Returns (raw)**: `ApiResult[GenericResponse, PostCheckAccountHolderErrorBody]`
- **Error**: `PostCheckAccountHolderErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PerformVerificationRequest` | `adyen/models/perform_verification_request.py` |
| `PerformVerificationRequestDict` | `adyen/models/perform_verification_request.py` |
| `GenericResponse` | `adyen/models/generic_response.py` |
| `PostCheckAccountHolderErrorBody` | `adyen/errors/post_check_account_holder_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.verification.post_delete_bank_accounts

- **Route**: `POST /deleteBankAccounts`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_delete_bank_accounts(*, body: DeleteBankAccountRequest | DeleteBankAccountRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenericResponse`
- **Returns (raw)**: `ApiResult[GenericResponse, PostDeleteBankAccountsErrorBody]`
- **Error**: `PostDeleteBankAccountsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteBankAccountRequest` | `adyen/models/delete_bank_account_request.py` |
| `DeleteBankAccountRequestDict` | `adyen/models/delete_bank_account_request.py` |
| `GenericResponse` | `adyen/models/generic_response.py` |
| `PostDeleteBankAccountsErrorBody` | `adyen/errors/post_delete_bank_accounts_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.verification.post_delete_legal_arrangements

- **Route**: `POST /deleteLegalArrangements`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_delete_legal_arrangements(*, body: DeleteLegalArrangementRequest | DeleteLegalArrangementRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenericResponse`
- **Returns (raw)**: `ApiResult[GenericResponse, PostDeleteLegalArrangementsErrorBody]`
- **Error**: `PostDeleteLegalArrangementsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteLegalArrangementRequest` | `adyen/models/delete_legal_arrangement_request.py` |
| `DeleteLegalArrangementRequestDict` | `adyen/models/delete_legal_arrangement_request.py` |
| `GenericResponse` | `adyen/models/generic_response.py` |
| `PostDeleteLegalArrangementsErrorBody` | `adyen/errors/post_delete_legal_arrangements_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.verification.post_delete_payout_methods

- **Route**: `POST /deletePayoutMethods`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_delete_payout_methods(*, body: DeletePayoutMethodRequest | DeletePayoutMethodRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenericResponse`
- **Returns (raw)**: `ApiResult[GenericResponse, PostDeletePayoutMethodsErrorBody]`
- **Error**: `PostDeletePayoutMethodsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeletePayoutMethodRequest` | `adyen/models/delete_payout_method_request.py` |
| `DeletePayoutMethodRequestDict` | `adyen/models/delete_payout_method_request.py` |
| `GenericResponse` | `adyen/models/generic_response.py` |
| `PostDeletePayoutMethodsErrorBody` | `adyen/errors/post_delete_payout_methods_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.verification.post_delete_shareholders

- **Route**: `POST /deleteShareholders`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_delete_shareholders(*, body: DeleteShareholderRequest | DeleteShareholderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenericResponse`
- **Returns (raw)**: `ApiResult[GenericResponse, PostDeleteShareholdersErrorBody]`
- **Error**: `PostDeleteShareholdersErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteShareholderRequest` | `adyen/models/delete_shareholder_request.py` |
| `DeleteShareholderRequestDict` | `adyen/models/delete_shareholder_request.py` |
| `GenericResponse` | `adyen/models/generic_response.py` |
| `PostDeleteShareholdersErrorBody` | `adyen/errors/post_delete_shareholders_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.verification.post_delete_signatories

- **Route**: `POST /deleteSignatories`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_delete_signatories(*, body: DeleteSignatoriesRequest | DeleteSignatoriesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenericResponse`
- **Returns (raw)**: `ApiResult[GenericResponse, PostDeleteSignatoriesErrorBody]`
- **Error**: `PostDeleteSignatoriesErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteSignatoriesRequest` | `adyen/models/delete_signatories_request.py` |
| `DeleteSignatoriesRequestDict` | `adyen/models/delete_signatories_request.py` |
| `GenericResponse` | `adyen/models/generic_response.py` |
| `PostDeleteSignatoriesErrorBody` | `adyen/errors/post_delete_signatories_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.verification.post_get_uploaded_documents

- **Route**: `POST /getUploadedDocuments`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_get_uploaded_documents(*, body: GetUploadedDocumentsRequest | GetUploadedDocumentsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetUploadedDocumentsResponse`
- **Returns (raw)**: `ApiResult[GetUploadedDocumentsResponse, PostGetUploadedDocumentsErrorBody]`
- **Error**: `PostGetUploadedDocumentsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetUploadedDocumentsRequest` | `adyen/models/get_uploaded_documents_request.py` |
| `GetUploadedDocumentsRequestDict` | `adyen/models/get_uploaded_documents_request.py` |
| `GetUploadedDocumentsResponse` | `adyen/models/get_uploaded_documents_response.py` |
| `PostGetUploadedDocumentsErrorBody` | `adyen/errors/post_get_uploaded_documents_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.verification.post_upload_document

- **Route**: `POST /uploadDocument`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_upload_document(*, body: UploadDocumentRequest | UploadDocumentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UpdateAccountHolderResponse`
- **Returns (raw)**: `ApiResult[UpdateAccountHolderResponse, PostUploadDocumentErrorBody]`
- **Error**: `PostUploadDocumentErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UploadDocumentRequest` | `adyen/models/upload_document_request.py` |
| `UploadDocumentRequestDict` | `adyen/models/upload_document_request.py` |
| `UpdateAccountHolderResponse` | `adyen/models/update_account_holder_response.py` |
| `PostUploadDocumentErrorBody` | `adyen/errors/post_upload_document_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

