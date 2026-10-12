<!-- Generated file — do not edit; regenerated with the SDK. -->

# Transfers — operations

Accessor: `client.transfers` · Source: `adyen/apis/transfers.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.transfers.get_transfers

- **Route**: `GET /transfers`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default14`
- **Signature**: `def get_transfers(created_since: RFC3339DateTime, created_until: RFC3339DateTime, *, balance_platform: str | None = None, account_holder_id: str | None = None, balance_account_id: str | None = None, payment_instrument_id: str | None = None, reference: str | None = None, category: Category2OrStr | None = None, sort_order: SortOrderOrStr | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `created_since`, `created_until`
- **Params**: `created_since` — query `createdSince` · `created_until` — query `createdUntil` · `balance_platform` — query `balancePlatform` · `account_holder_id` — query `accountHolderId` · `balance_account_id` — query `balanceAccountId` · `payment_instrument_id` — query `paymentInstrumentId` · `reference` — query · `category` — query · `sort_order` — query `sortOrder` · `cursor` — query · `limit` — query
- **Returns (parsed)**: `FindTransfersResponse`
- **Returns (raw)**: `ApiResult[FindTransfersResponse, GetTransfersErrorBody]`
- **Error**: `GetTransfersErrorBody` — **Case A (typed)**
- **Error arms**: `TransferServiceRestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Category2OrStr` | `adyen/models/enums/category2.py` |
| `SortOrderOrStr` | `adyen/models/enums/sort_order.py` |
| `FindTransfersResponse` | `adyen/models/find_transfers_response.py` |
| `GetTransfersErrorBody` | `adyen/errors/get_transfers_error.py` |
| `TransferServiceRestServiceError` | `adyen/models/transfer_service_rest_service_error.py` |

### client.transfers.get_transfers_id

- **Route**: `GET /transfers/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default14`
- **Signature**: `def get_transfers_id(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `TransferData`
- **Returns (raw)**: `ApiResult[TransferData, GetTransfersIdErrorBody]`
- **Error**: `GetTransfersIdErrorBody` — **Case A (typed)**
- **Error arms**: `TransferServiceRestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransferData` | `adyen/models/transfer_data.py` |
| `GetTransfersIdErrorBody` | `adyen/errors/get_transfers_id_error.py` |
| `TransferServiceRestServiceError` | `adyen/models/transfer_service_rest_service_error.py` |

### client.transfers.post_transfers

- **Route**: `POST /transfers`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default14`
- **Signature**: `def post_transfers(*, idempotency_key: str | None = None, www_authenticate: str | None = None, body: TransferInfo | TransferInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `www_authenticate` — header `WWW-Authenticate` · `body` — JSON body
- **Returns (parsed)**: `Transfer`
- **Returns (raw)**: `ApiResult[Transfer, PostTransfersErrorBody]`
- **Error**: `PostTransfersErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [401] · `TransferServiceRestServiceError` [403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransferInfo` | `adyen/models/transfer_info.py` |
| `TransferInfoDict` | `adyen/models/transfer_info.py` |
| `Transfer` | `adyen/models/transfer.py` |
| `PostTransfersErrorBody` | `adyen/errors/post_transfers_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |
| `TransferServiceRestServiceError` | `adyen/models/transfer_service_rest_service_error.py` |

### client.transfers.post_transfers_approve

- **Route**: `POST /transfers/approve`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default14`
- **Signature**: `def post_transfers_approve(*, idempotency_key: str | None = None, www_authenticate: str | None = None, body: ApproveTransfersRequest | ApproveTransfersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `www_authenticate` — header `WWW-Authenticate` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, PostTransfersApproveErrorBody]`
- **Error**: `PostTransfersApproveErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [401] · `TransferServiceRestServiceError` [403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApproveTransfersRequest` | `adyen/models/approve_transfers_request.py` |
| `ApproveTransfersRequestDict` | `adyen/models/approve_transfers_request.py` |
| `PostTransfersApproveErrorBody` | `adyen/errors/post_transfers_approve_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |
| `TransferServiceRestServiceError` | `adyen/models/transfer_service_rest_service_error.py` |

### client.transfers.post_transfers_cancel

- **Route**: `POST /transfers/cancel`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default14`
- **Signature**: `def post_transfers_cancel(*, idempotency_key: str | None = None, body: CancelTransfersRequest | CancelTransfersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, PostTransfersCancelErrorBody]`
- **Error**: `PostTransfersCancelErrorBody` — **Case A (typed)**
- **Error arms**: `TransferServiceRestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelTransfersRequest` | `adyen/models/cancel_transfers_request.py` |
| `CancelTransfersRequestDict` | `adyen/models/cancel_transfers_request.py` |
| `PostTransfersCancelErrorBody` | `adyen/errors/post_transfers_cancel_error.py` |
| `TransferServiceRestServiceError` | `adyen/models/transfer_service_rest_service_error.py` |

### client.transfers.post_transfers_transfer_id_returns

- **Route**: `POST /transfers/{transferId}/returns`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default14`
- **Signature**: `def post_transfers_transfer_id_returns(transfer_id: str, *, idempotency_key: str | None = None, body: ReturnTransferRequest | ReturnTransferRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transfer_id`
- **Params**: `transfer_id` — path `transferId` · `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `ReturnTransferResponse`
- **Returns (raw)**: `ApiResult[ReturnTransferResponse, PostTransfersTransferIdReturnsErrorBody]`
- **Error**: `PostTransfersTransferIdReturnsErrorBody` — **Case A (typed)**
- **Error arms**: `TransferServiceRestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ReturnTransferRequest` | `adyen/models/return_transfer_request.py` |
| `ReturnTransferRequestDict` | `adyen/models/return_transfer_request.py` |
| `ReturnTransferResponse` | `adyen/models/return_transfer_response.py` |
| `PostTransfersTransferIdReturnsErrorBody` | `adyen/errors/post_transfers_transfer_id_returns_error.py` |
| `TransferServiceRestServiceError` | `adyen/models/transfer_service_rest_service_error.py` |

