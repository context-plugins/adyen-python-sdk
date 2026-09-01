<!-- Generated file — do not edit; regenerated with the SDK. -->

# BalanceAccounts — operations

Accessor: `client.balance_accounts` · Source: `adyen/apis/balance_accounts.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.balance_accounts.get_balance_accounts_id

- **Route**: `GET /balanceAccounts/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_balance_accounts_id(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `BalanceAccount`
- **Returns (raw)**: `ApiResult[BalanceAccount, GetBalanceAccountsIdErrorBody]`
- **Error**: `GetBalanceAccountsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceAccount` | `adyen/models/balance_account.py` |
| `GetBalanceAccountsIdErrorBody` | `adyen/errors/get_balance_accounts_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.balance_accounts.get_balance_accounts_id_payment_instruments

- **Route**: `GET /balanceAccounts/{id}/paymentInstruments`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_balance_accounts_id_payment_instruments(id: str, *, offset: int | None = None, limit: int | None = None, status: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `offset` — query · `limit` — query · `status` — query
- **Returns (parsed)**: `PaginatedPaymentInstrumentsResponse`
- **Returns (raw)**: `ApiResult[PaginatedPaymentInstrumentsResponse, GetBalanceAccountsIdPaymentInstrumentsErrorBody]`
- **Error**: `GetBalanceAccountsIdPaymentInstrumentsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaginatedPaymentInstrumentsResponse` | `adyen/models/paginated_payment_instruments_response.py` |
| `GetBalanceAccountsIdPaymentInstrumentsErrorBody` | `adyen/errors/get_balance_accounts_id_payment_instruments_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.balance_accounts.get_balance_accounts_id_transaction_rules

- **Route**: `GET /balanceAccounts/{id}/transactionRules`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_balance_accounts_id_transaction_rules(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `TransactionRulesResponse`
- **Returns (raw)**: `ApiResult[TransactionRulesResponse, GetBalanceAccountsIdTransactionRulesErrorBody]`
- **Error**: `GetBalanceAccountsIdTransactionRulesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransactionRulesResponse` | `adyen/models/transaction_rules_response.py` |
| `GetBalanceAccountsIdTransactionRulesErrorBody` | `adyen/errors/get_balance_accounts_id_transaction_rules_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.balance_accounts.patch_balance_accounts_id

- **Route**: `PATCH /balanceAccounts/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def patch_balance_accounts_id(id: str, *, body: BalanceAccountUpdateRequest | BalanceAccountUpdateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `BalanceAccount`
- **Returns (raw)**: `ApiResult[BalanceAccount, PatchBalanceAccountsIdErrorBody]`
- **Error**: `PatchBalanceAccountsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceAccountUpdateRequest` | `adyen/models/balance_account_update_request.py` |
| `BalanceAccountUpdateRequestDict` | `adyen/models/balance_account_update_request.py` |
| `BalanceAccount` | `adyen/models/balance_account.py` |
| `PatchBalanceAccountsIdErrorBody` | `adyen/errors/patch_balance_accounts_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.balance_accounts.post_balance_accounts

- **Route**: `POST /balanceAccounts`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_balance_accounts(*, body: BalanceAccountInfo | BalanceAccountInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BalanceAccount`
- **Returns (raw)**: `ApiResult[BalanceAccount, PostBalanceAccountsErrorBody]`
- **Error**: `PostBalanceAccountsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceAccountInfo` | `adyen/models/balance_account_info.py` |
| `BalanceAccountInfoDict` | `adyen/models/balance_account_info.py` |
| `BalanceAccount` | `adyen/models/balance_account.py` |
| `PostBalanceAccountsErrorBody` | `adyen/errors/post_balance_accounts_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

