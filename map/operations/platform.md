<!-- Generated file — do not edit; regenerated with the SDK. -->

# Platform — operations

Accessor: `client.platform` · Source: `adyen/apis/platform.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.platform.get_balance_platforms_id

- **Route**: `GET /balancePlatforms/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_balance_platforms_id(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `BalancePlatform`
- **Returns (raw)**: `ApiResult[BalancePlatform, GetBalancePlatformsIdErrorBody]`
- **Error**: `GetBalancePlatformsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalancePlatform` | `adyen/models/balance_platform.py` |
| `GetBalancePlatformsIdErrorBody` | `adyen/errors/get_balance_platforms_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.platform.get_balance_platforms_id_account_holders

- **Route**: `GET /balancePlatforms/{id}/accountHolders`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_balance_platforms_id_account_holders(id: str, *, offset: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `offset` — query · `limit` — query
- **Returns (parsed)**: `PaginatedAccountHoldersResponse`
- **Returns (raw)**: `ApiResult[PaginatedAccountHoldersResponse, GetBalancePlatformsIdAccountHoldersErrorBody]`
- **Error**: `GetBalancePlatformsIdAccountHoldersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaginatedAccountHoldersResponse` | `adyen/models/paginated_account_holders_response.py` |
| `GetBalancePlatformsIdAccountHoldersErrorBody` | `adyen/errors/get_balance_platforms_id_account_holders_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.platform.get_balance_platforms_id_transaction_rules

- **Route**: `GET /balancePlatforms/{id}/transactionRules`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_balance_platforms_id_transaction_rules(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `TransactionRulesResponse`
- **Returns (raw)**: `ApiResult[TransactionRulesResponse, GetBalancePlatformsIdTransactionRulesErrorBody]`
- **Error**: `GetBalancePlatformsIdTransactionRulesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransactionRulesResponse` | `adyen/models/transaction_rules_response.py` |
| `GetBalancePlatformsIdTransactionRulesErrorBody` | `adyen/errors/get_balance_platforms_id_transaction_rules_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

