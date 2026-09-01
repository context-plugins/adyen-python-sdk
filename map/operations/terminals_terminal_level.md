<!-- Generated file — do not edit; regenerated with the SDK. -->

# TerminalsTerminalLevel — operations

Accessor: `client.terminals_terminal_level` · Source: `adyen/apis/terminals_terminal_level.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.terminals_terminal_level.get_terminals

- **Route**: `GET /terminals`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_terminals(*, search_query: str | None = None, otp_query: str | None = None, countries: str | None = None, merchant_ids: str | None = None, store_ids: str | None = None, brand_models: str | None = None, page_number: int | None = None, page_size: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `search_query` — query `searchQuery` · `otp_query` — query `otpQuery` · `countries` — query · `merchant_ids` — query `merchantIds` · `store_ids` — query `storeIds` · `brand_models` — query `brandModels` · `page_number` — query `pageNumber` · `page_size` — query `pageSize`
- **Returns (parsed)**: `ListTerminalsResponse`
- **Returns (raw)**: `ApiResult[ListTerminalsResponse, GetTerminalsErrorBody]`
- **Error**: `GetTerminalsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListTerminalsResponse` | `adyen/models/list_terminals_response.py` |
| `GetTerminalsErrorBody` | `adyen/errors/get_terminals_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminals_terminal_level.post_terminals_terminal_id_reassign

- **Route**: `POST /terminals/{terminalId}/reassign`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_terminals_terminal_id_reassign(terminal_id: str, *, body: TerminalReassignmentRequest | TerminalReassignmentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `terminal_id`
- **Params**: `terminal_id` — path `terminalId` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PostTerminalsTerminalIdReassignErrorBody]`
- **Error**: `PostTerminalsTerminalIdReassignErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalReassignmentRequest` | `adyen/models/terminal_reassignment_request.py` |
| `TerminalReassignmentRequestDict` | `adyen/models/terminal_reassignment_request.py` |
| `PostTerminalsTerminalIdReassignErrorBody` | `adyen/errors/post_terminals_terminal_id_reassign_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

