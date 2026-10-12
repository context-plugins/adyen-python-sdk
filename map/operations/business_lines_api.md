<!-- Generated file — do not edit; regenerated with the SDK. -->

# BusinessLinesApi — operations

Accessor: `client.business_lines_api` · Source: `adyen/apis/business_lines_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.business_lines_api.delete_business_lines_id

- **Route**: `DELETE /businessLines/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def delete_business_lines_id(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteBusinessLinesIdErrorBody]`
- **Error**: `DeleteBusinessLinesIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteBusinessLinesIdErrorBody` | `adyen/errors/delete_business_lines_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.business_lines_api.get_business_lines_id

- **Route**: `GET /businessLines/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def get_business_lines_id(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `BusinessLine`
- **Returns (raw)**: `ApiResult[BusinessLine, GetBusinessLinesIdErrorBody]`
- **Error**: `GetBusinessLinesIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BusinessLine` | `adyen/models/business_line.py` |
| `GetBusinessLinesIdErrorBody` | `adyen/errors/get_business_lines_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.business_lines_api.patch_business_lines_id

- **Route**: `PATCH /businessLines/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def patch_business_lines_id(id_: str, *, body: BusinessLineInfoUpdate | BusinessLineInfoUpdateDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `BusinessLine`
- **Returns (raw)**: `ApiResult[BusinessLine, PatchBusinessLinesIdErrorBody]`
- **Error**: `PatchBusinessLinesIdErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BusinessLineInfoUpdate` | `adyen/models/business_line_info_update.py` |
| `BusinessLineInfoUpdateDict` | `adyen/models/business_line_info_update.py` |
| `BusinessLine` | `adyen/models/business_line.py` |
| `PatchBusinessLinesIdErrorBody` | `adyen/errors/patch_business_lines_id_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.business_lines_api.post_business_lines

- **Route**: `POST /businessLines`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default18`
- **Signature**: `def post_business_lines(*, body: BusinessLineInfo | BusinessLineInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BusinessLine`
- **Returns (raw)**: `ApiResult[BusinessLine, PostBusinessLinesErrorBody]`
- **Error**: `PostBusinessLinesErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BusinessLineInfo` | `adyen/models/business_line_info.py` |
| `BusinessLineInfoDict` | `adyen/models/business_line_info.py` |
| `BusinessLine` | `adyen/models/business_line.py` |
| `PostBusinessLinesErrorBody` | `adyen/errors/post_business_lines_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

