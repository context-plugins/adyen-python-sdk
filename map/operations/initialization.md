<!-- Generated file — do not edit; regenerated with the SDK. -->

# Initialization — operations

Accessor: `client.initialization` · Source: `adyen/apis/initialization.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.initialization.post_store_detail

- **Route**: `POST /storeDetail`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default3`
- **Signature**: `def post_store_detail(*, body: StoreDetailRequest | StoreDetailRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StoreDetailResponse`
- **Returns (raw)**: `ApiResult[StoreDetailResponse, PostStoreDetailErrorBody]`
- **Error**: `PostStoreDetailErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StoreDetailRequest` | `adyen/models/store_detail_request.py` |
| `StoreDetailRequestDict` | `adyen/models/store_detail_request.py` |
| `StoreDetailResponse` | `adyen/models/store_detail_response.py` |
| `PostStoreDetailErrorBody` | `adyen/errors/post_store_detail_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.initialization.post_store_detail_and_submit_third_party

- **Route**: `POST /storeDetailAndSubmitThirdParty`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default3`
- **Signature**: `def post_store_detail_and_submit_third_party(*, body: StoreDetailAndSubmitRequest | StoreDetailAndSubmitRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StoreDetailAndSubmitResponse`
- **Returns (raw)**: `ApiResult[StoreDetailAndSubmitResponse, PostStoreDetailAndSubmitThirdPartyErrorBody]`
- **Error**: `PostStoreDetailAndSubmitThirdPartyErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StoreDetailAndSubmitRequest` | `adyen/models/store_detail_and_submit_request.py` |
| `StoreDetailAndSubmitRequestDict` | `adyen/models/store_detail_and_submit_request.py` |
| `StoreDetailAndSubmitResponse` | `adyen/models/store_detail_and_submit_response.py` |
| `PostStoreDetailAndSubmitThirdPartyErrorBody` | `adyen/errors/post_store_detail_and_submit_third_party_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.initialization.post_submit_third_party

- **Route**: `POST /submitThirdParty`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default3`
- **Signature**: `def post_submit_third_party(*, body: SubmitRequest | SubmitRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SubmitResponse`
- **Returns (raw)**: `ApiResult[SubmitResponse, PostSubmitThirdPartyErrorBody]`
- **Error**: `PostSubmitThirdPartyErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubmitRequest` | `adyen/models/submit_request.py` |
| `SubmitRequestDict` | `adyen/models/submit_request.py` |
| `SubmitResponse` | `adyen/models/submit_response.py` |
| `PostSubmitThirdPartyErrorBody` | `adyen/errors/post_submit_third_party_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

