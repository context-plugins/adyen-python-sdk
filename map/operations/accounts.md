<!-- Generated file — do not edit; regenerated with the SDK. -->

# Accounts — operations

Accessor: `client.accounts` · Source: `adyen/apis/accounts.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.accounts.post_close_account

- **Route**: `POST /closeAccount`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_close_account(*, body: CloseAccountRequest | CloseAccountRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CloseAccountResponse`
- **Returns (raw)**: `ApiResult[CloseAccountResponse, PostCloseAccountErrorBody]`
- **Error**: `PostCloseAccountErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CloseAccountRequest` | `adyen/models/close_account_request.py` |
| `CloseAccountRequestDict` | `adyen/models/close_account_request.py` |
| `CloseAccountResponse` | `adyen/models/close_account_response.py` |
| `PostCloseAccountErrorBody` | `adyen/errors/post_close_account_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.accounts.post_create_account

- **Route**: `POST /createAccount`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_create_account(*, body: CreateAccountRequest | CreateAccountRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateAccountResponse`
- **Returns (raw)**: `ApiResult[CreateAccountResponse, PostCreateAccountErrorBody]`
- **Error**: `PostCreateAccountErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateAccountRequest` | `adyen/models/create_account_request.py` |
| `CreateAccountRequestDict` | `adyen/models/create_account_request.py` |
| `CreateAccountResponse` | `adyen/models/create_account_response.py` |
| `PostCreateAccountErrorBody` | `adyen/errors/post_create_account_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.accounts.post_update_account

- **Route**: `POST /updateAccount`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_update_account(*, body: UpdateAccountRequest | UpdateAccountRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UpdateAccountResponse`
- **Returns (raw)**: `ApiResult[UpdateAccountResponse, PostUpdateAccountErrorBody]`
- **Error**: `PostUpdateAccountErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateAccountRequest` | `adyen/models/update_account_request.py` |
| `UpdateAccountRequestDict` | `adyen/models/update_account_request.py` |
| `UpdateAccountResponse` | `adyen/models/update_account_response.py` |
| `PostUpdateAccountErrorBody` | `adyen/errors/post_update_account_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

