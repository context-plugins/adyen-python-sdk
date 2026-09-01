<!-- Generated file — do not edit; regenerated with the SDK. -->

# RaiseDisputes — operations

Accessor: `client.raise_disputes` · Source: `adyen/apis/raise_disputes.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.raise_disputes.get_disputes

- **Route**: `GET /disputes`
- **Server**: `default23`
- **Signature**: `def get_disputes(*, status: str | None = None, payment_instrument: str | None = None, created_since: str | None = None, created_until: str | None = None, offset: str | None = None, limit: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query · `payment_instrument` — query `paymentInstrument` · `created_since` — query `createdSince` · `created_until` — query `createdUntil` · `offset` — query · `limit` — query
- **Returns (parsed)**: `list[list[DisputeResponse]]`
- **Returns (raw)**: `ApiResult[list[list[DisputeResponse]], GetDisputesErrorBody]`
- **Error**: `GetDisputesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisputeResponse` | `adyen/models/dispute_response.py` |
| `GetDisputesErrorBody` | `adyen/errors/get_disputes_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.raise_disputes.get_disputes_id

- **Route**: `GET /disputes/{id}`
- **Server**: `default23`
- **Signature**: `def get_disputes_id(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `DisputeResponse`
- **Returns (raw)**: `ApiResult[DisputeResponse, GetDisputesIdErrorBody]`
- **Error**: `GetDisputesIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisputeResponse` | `adyen/models/dispute_response.py` |
| `GetDisputesIdErrorBody` | `adyen/errors/get_disputes_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.raise_disputes.patch_disputes_id

- **Route**: `PATCH /disputes/{id}`
- **Server**: `default23`
- **Signature**: `def patch_disputes_id(id: str, *, body: PatchableDisputeRequest | PatchableDisputeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `DisputeResponse`
- **Returns (raw)**: `ApiResult[DisputeResponse, PatchDisputesIdErrorBody]`
- **Error**: `PatchDisputesIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PatchableDisputeRequest` | `adyen/models/patchable_dispute_request.py` |
| `PatchableDisputeRequestDict` | `adyen/models/patchable_dispute_request.py` |
| `DisputeResponse` | `adyen/models/dispute_response.py` |
| `PatchDisputesIdErrorBody` | `adyen/errors/patch_disputes_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.raise_disputes.post_disputes

- **Route**: `POST /disputes`
- **Server**: `default23`
- **Signature**: `def post_disputes(body: DisputeRequest | DisputeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DisputeResponse`
- **Returns (raw)**: `ApiResult[DisputeResponse, PostDisputesErrorBody]`
- **Error**: `PostDisputesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisputeRequest` | `adyen/models/dispute_request.py` |
| `DisputeRequestDict` | `adyen/models/dispute_request.py` |
| `DisputeResponse` | `adyen/models/dispute_response.py` |
| `PostDisputesErrorBody` | `adyen/errors/post_disputes_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

