<!-- Generated file — do not edit; regenerated with the SDK. -->

# MyApiCredential — operations

Accessor: `client.my_api_credential` · Source: `adyen/apis/my_api_credential.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.my_api_credential.delete_me_allowed_origins_origin_id

- **Route**: `DELETE /me/allowedOrigins/{originId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def delete_me_allowed_origins_origin_id(origin_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `origin_id`
- **Params**: `origin_id` — path `originId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteMeAllowedOriginsOriginIdErrorBody]`
- **Error**: `DeleteMeAllowedOriginsOriginIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteMeAllowedOriginsOriginIdErrorBody` | `adyen/errors/delete_me_allowed_origins_origin_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.my_api_credential.get_me

- **Route**: `GET /me`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_me(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `MeApiCredential`
- **Returns (raw)**: `ApiResult[MeApiCredential, GetMeErrorBody]`
- **Error**: `GetMeErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeApiCredential` | `adyen/models/me_api_credential.py` |
| `GetMeErrorBody` | `adyen/errors/get_me_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.my_api_credential.get_me_allowed_origins

- **Route**: `GET /me/allowedOrigins`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_me_allowed_origins(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `AllowedOriginsResponse`
- **Returns (raw)**: `ApiResult[AllowedOriginsResponse, GetMeAllowedOriginsErrorBody]`
- **Error**: `GetMeAllowedOriginsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AllowedOriginsResponse` | `adyen/models/allowed_origins_response.py` |
| `GetMeAllowedOriginsErrorBody` | `adyen/errors/get_me_allowed_origins_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.my_api_credential.get_me_allowed_origins_origin_id

- **Route**: `GET /me/allowedOrigins/{originId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_me_allowed_origins_origin_id(origin_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `origin_id`
- **Params**: `origin_id` — path `originId`
- **Returns (parsed)**: `AllowedOrigin`
- **Returns (raw)**: `ApiResult[AllowedOrigin, GetMeAllowedOriginsOriginIdErrorBody]`
- **Error**: `GetMeAllowedOriginsOriginIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AllowedOrigin` | `adyen/models/allowed_origin.py` |
| `GetMeAllowedOriginsOriginIdErrorBody` | `adyen/errors/get_me_allowed_origins_origin_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.my_api_credential.post_me_allowed_origins

- **Route**: `POST /me/allowedOrigins`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_me_allowed_origins(*, body: CreateAllowedOriginRequest | CreateAllowedOriginRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AllowedOrigin`
- **Returns (raw)**: `ApiResult[AllowedOrigin, PostMeAllowedOriginsErrorBody]`
- **Error**: `PostMeAllowedOriginsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateAllowedOriginRequest` | `adyen/models/create_allowed_origin_request.py` |
| `CreateAllowedOriginRequestDict` | `adyen/models/create_allowed_origin_request.py` |
| `AllowedOrigin` | `adyen/models/allowed_origin.py` |
| `PostMeAllowedOriginsErrorBody` | `adyen/errors/post_me_allowed_origins_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.my_api_credential.post_me_generate_client_key

- **Route**: `POST /me/generateClientKey`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_me_generate_client_key(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `GenerateClientKeyResponse`
- **Returns (raw)**: `ApiResult[GenerateClientKeyResponse, PostMeGenerateClientKeyErrorBody]`
- **Error**: `PostMeGenerateClientKeyErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateClientKeyResponse` | `adyen/models/generate_client_key_response.py` |
| `PostMeGenerateClientKeyErrorBody` | `adyen/errors/post_me_generate_client_key_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

