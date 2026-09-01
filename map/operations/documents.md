<!-- Generated file — do not edit; regenerated with the SDK. -->

# Documents — operations

Accessor: `client.documents` · Source: `adyen/apis/documents.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.documents.delete_documents_id

- **Route**: `DELETE /documents/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def delete_documents_id(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteDocumentsIdErrorBody]`
- **Error**: `DeleteDocumentsIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteDocumentsIdErrorBody` | `adyen/errors/delete_documents_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.documents.get_documents_id

- **Route**: `GET /documents/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_documents_id(id: str, *, skip_content: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `skip_content` — query `skipContent`
- **Returns (parsed)**: `Document`
- **Returns (raw)**: `ApiResult[Document, GetDocumentsIdErrorBody]`
- **Error**: `GetDocumentsIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Document` | `adyen/models/document.py` |
| `GetDocumentsIdErrorBody` | `adyen/errors/get_documents_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.documents.patch_documents_id

- **Route**: `PATCH /documents/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def patch_documents_id(id: str, *, x_requested_verification_code: str | None = None, body: Document | DocumentDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `x_requested_verification_code` — header `x-requested-verification-code` · `body` — JSON body
- **Returns (parsed)**: `Document`
- **Returns (raw)**: `ApiResult[Document, PatchDocumentsIdErrorBody]`
- **Error**: `PatchDocumentsIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Document` | `adyen/models/document.py` |
| `DocumentDict` | `adyen/models/document.py` |
| `PatchDocumentsIdErrorBody` | `adyen/errors/patch_documents_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.documents.post_documents

- **Route**: `POST /documents`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_documents(*, x_requested_verification_code: str | None = None, body: Document | DocumentDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `x_requested_verification_code` — header `x-requested-verification-code` · `body` — JSON body
- **Returns (parsed)**: `Document`
- **Returns (raw)**: `ApiResult[Document, PostDocumentsErrorBody]`
- **Error**: `PostDocumentsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Document` | `adyen/models/document.py` |
| `DocumentDict` | `adyen/models/document.py` |
| `PostDocumentsErrorBody` | `adyen/errors/post_documents_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

