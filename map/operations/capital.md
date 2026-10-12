<!-- Generated file — do not edit; regenerated with the SDK. -->

# Capital — operations

Accessor: `client.capital` · Source: `adyen/apis/capital.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.capital.get_grants

- **Route**: `GET /grants`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default14`
- **Signature**: `def get_grants(*, counterparty_account_holder_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `counterparty_account_holder_id` — query `counterpartyAccountHolderId`
- **Returns (parsed)**: `CapitalGrants`
- **Returns (raw)**: `ApiResult[CapitalGrants, GetGrantsErrorBody]`
- **Error**: `GetGrantsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CapitalGrants` | `adyen/models/capital_grants.py` |
| `GetGrantsErrorBody` | `adyen/errors/get_grants_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.capital.get_grants_id

- **Route**: `GET /grants/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default14`
- **Signature**: `def get_grants_id(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `CapitalGrant`
- **Returns (raw)**: `ApiResult[CapitalGrant, GetGrantsIdErrorBody]`
- **Error**: `GetGrantsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CapitalGrant` | `adyen/models/capital_grant.py` |
| `GetGrantsIdErrorBody` | `adyen/errors/get_grants_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.capital.post_grants

- **Route**: `POST /grants`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default14`
- **Signature**: `def post_grants(*, idempotency_key: str | None = None, body: CapitalGrantInfo | CapitalGrantInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `idempotency_key` — header `Idempotency-Key` · `body` — JSON body
- **Returns (parsed)**: `CapitalGrant`
- **Returns (raw)**: `ApiResult[CapitalGrant, PostGrantsErrorBody]`
- **Error**: `PostGrantsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CapitalGrantInfo` | `adyen/models/capital_grant_info.py` |
| `CapitalGrantInfoDict` | `adyen/models/capital_grant_info.py` |
| `CapitalGrant` | `adyen/models/capital_grant.py` |
| `PostGrantsErrorBody` | `adyen/errors/post_grants_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

