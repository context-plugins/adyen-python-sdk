<!-- Generated file — do not edit; regenerated with the SDK. -->

# GrantAccounts — operations

Accessor: `client.grant_accounts` · Source: `adyen/apis/grant_accounts.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.grant_accounts.get_grant_accounts_id

- **Route**: `GET /grantAccounts/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_grant_accounts_id(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `CapitalGrantAccount`
- **Returns (raw)**: `ApiResult[CapitalGrantAccount, GetGrantAccountsIdErrorBody]`
- **Error**: `GetGrantAccountsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CapitalGrantAccount` | `adyen/models/capital_grant_account.py` |
| `GetGrantAccountsIdErrorBody` | `adyen/errors/get_grant_accounts_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.grant_accounts.get_grant_accounts_id1

- **Route**: `GET /grantAccounts/{id}`
- **Server**: `default15`
- **Signature**: `def get_grant_accounts_id1(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `GrantAccount`
- **Returns (raw)**: `ApiResult[GrantAccount, GetGrantAccountsId1ErrorBody]`
- **Error**: `GetGrantAccountsId1ErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [404, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GrantAccount` | `adyen/models/grant_account.py` |
| `GetGrantAccountsId1ErrorBody` | `adyen/errors/get_grant_accounts_id1_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

