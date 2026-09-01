<!-- Generated file — do not edit; regenerated with the SDK. -->

# Transactions — operations

Accessor: `client.transactions` · Source: `adyen/apis/transactions.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.transactions.get_transactions

- **Route**: `GET /transactions`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default14`
- **Signature**: `def get_transactions(created_since: RFC3339DateTime, created_until: RFC3339DateTime, *, balance_platform: str | None = None, payment_instrument_id: str | None = None, account_holder_id: str | None = None, balance_account_id: str | None = None, cursor: str | None = None, sort_order: SortOrderOrStr | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `created_since`, `created_until`
- **Params**: `created_since` — query `createdSince` · `created_until` — query `createdUntil` · `balance_platform` — query `balancePlatform` · `payment_instrument_id` — query `paymentInstrumentId` · `account_holder_id` — query `accountHolderId` · `balance_account_id` — query `balanceAccountId` · `cursor` — query · `sort_order` — query `sortOrder` · `limit` — query
- **Returns (parsed)**: `TransactionSearchResponse`
- **Returns (raw)**: `ApiResult[TransactionSearchResponse, GetTransactionsErrorBody]`
- **Error**: `GetTransactionsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SortOrderOrStr` | `adyen/models/enums/sort_order.py` |
| `TransactionSearchResponse` | `adyen/models/transaction_search_response.py` |
| `GetTransactionsErrorBody` | `adyen/errors/get_transactions_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.transactions.get_transactions_id

- **Route**: `GET /transactions/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default14`
- **Signature**: `def get_transactions_id(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `Transaction`
- **Returns (raw)**: `ApiResult[Transaction, GetTransactionsIdErrorBody]`
- **Error**: `GetTransactionsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Transaction` | `adyen/models/transaction.py` |
| `GetTransactionsIdErrorBody` | `adyen/errors/get_transactions_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

