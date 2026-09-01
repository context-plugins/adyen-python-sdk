<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersMerchantLevel — operations

Accessor: `client.users_merchant_level` · Source: `adyen/apis/users_merchant_level.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users_merchant_level.get_merchants_merchant_id_users

- **Route**: `GET /merchants/{merchantId}/users`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_users(merchant_id: str, *, page_number: int | None = None, page_size: int | None = None, username: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize` · `username` — query
- **Returns (parsed)**: `ListMerchantUsersResponse`
- **Returns (raw)**: `ApiResult[ListMerchantUsersResponse, GetMerchantsMerchantIdUsersErrorBody]`
- **Error**: `GetMerchantsMerchantIdUsersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListMerchantUsersResponse` | `adyen/models/list_merchant_users_response.py` |
| `GetMerchantsMerchantIdUsersErrorBody` | `adyen/errors/get_merchants_merchant_id_users_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.users_merchant_level.get_merchants_merchant_id_users_user_id

- **Route**: `GET /merchants/{merchantId}/users/{userId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_users_user_id(merchant_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `user_id`
- **Params**: `merchant_id` — path `merchantId` · `user_id` — path `userId`
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, GetMerchantsMerchantIdUsersUserIdErrorBody]`
- **Error**: `GetMerchantsMerchantIdUsersUserIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `User` | `adyen/models/user.py` |
| `GetMerchantsMerchantIdUsersUserIdErrorBody` | `adyen/errors/get_merchants_merchant_id_users_user_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.users_merchant_level.patch_merchants_merchant_id_users_user_id

- **Route**: `PATCH /merchants/{merchantId}/users/{userId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_users_user_id(merchant_id: str, user_id: str, *, body: UpdateMerchantUserRequest | UpdateMerchantUserRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `user_id`
- **Params**: `merchant_id` — path `merchantId` · `user_id` — path `userId` · `body` — JSON body
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, PatchMerchantsMerchantIdUsersUserIdErrorBody]`
- **Error**: `PatchMerchantsMerchantIdUsersUserIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateMerchantUserRequest` | `adyen/models/update_merchant_user_request.py` |
| `UpdateMerchantUserRequestDict` | `adyen/models/update_merchant_user_request.py` |
| `User` | `adyen/models/user.py` |
| `PatchMerchantsMerchantIdUsersUserIdErrorBody` | `adyen/errors/patch_merchants_merchant_id_users_user_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.users_merchant_level.post_merchants_merchant_id_users

- **Route**: `POST /merchants/{merchantId}/users`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_users(merchant_id: str, *, body: CreateMerchantUserRequest | CreateMerchantUserRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `body` — JSON body
- **Returns (parsed)**: `CreateUserResponse`
- **Returns (raw)**: `ApiResult[CreateUserResponse, PostMerchantsMerchantIdUsersErrorBody]`
- **Error**: `PostMerchantsMerchantIdUsersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateMerchantUserRequest` | `adyen/models/create_merchant_user_request.py` |
| `CreateMerchantUserRequestDict` | `adyen/models/create_merchant_user_request.py` |
| `CreateUserResponse` | `adyen/models/create_user_response.py` |
| `PostMerchantsMerchantIdUsersErrorBody` | `adyen/errors/post_merchants_merchant_id_users_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

