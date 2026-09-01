<!-- Generated file — do not edit; regenerated with the SDK. -->

# AllowedOriginsMerchantLevel — operations

Accessor: `client.allowed_origins_merchant_level` · Source: `adyen/apis/allowed_origins_merchant_level.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.allowed_origins_merchant_level.delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id

- **Route**: `DELETE /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(merchant_id: str, api_credential_id: str, origin_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `api_credential_id`, `origin_id`
- **Params**: `merchant_id` — path `merchantId` · `api_credential_id` — path `apiCredentialId` · `origin_id` — path `originId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody]`
- **Error**: `DeleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody` | `adyen/errors/delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.allowed_origins_merchant_level.get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins

- **Route**: `GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `api_credential_id`
- **Params**: `merchant_id` — path `merchantId` · `api_credential_id` — path `apiCredentialId`
- **Returns (parsed)**: `AllowedOriginsResponse`
- **Returns (raw)**: `ApiResult[AllowedOriginsResponse, GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody]`
- **Error**: `GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AllowedOriginsResponse` | `adyen/models/allowed_origins_response.py` |
| `GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody` | `adyen/errors/get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.allowed_origins_merchant_level.get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id

- **Route**: `GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(merchant_id: str, api_credential_id: str, origin_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `api_credential_id`, `origin_id`
- **Params**: `merchant_id` — path `merchantId` · `api_credential_id` — path `apiCredentialId` · `origin_id` — path `originId`
- **Returns (parsed)**: `AllowedOrigin`
- **Returns (raw)**: `ApiResult[AllowedOrigin, GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody]`
- **Error**: `GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AllowedOrigin` | `adyen/models/allowed_origin.py` |
| `GetMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody` | `adyen/errors/get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.allowed_origins_merchant_level.post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins

- **Route**: `POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(merchant_id: str, api_credential_id: str, *, body: AllowedOrigin | AllowedOriginDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `api_credential_id`
- **Params**: `merchant_id` — path `merchantId` · `api_credential_id` — path `apiCredentialId` · `body` — JSON body
- **Returns (parsed)**: `AllowedOrigin`
- **Returns (raw)**: `ApiResult[AllowedOrigin, PostMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody]`
- **Error**: `PostMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AllowedOrigin` | `adyen/models/allowed_origin.py` |
| `AllowedOriginDict` | `adyen/models/allowed_origin.py` |
| `PostMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody` | `adyen/errors/post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

