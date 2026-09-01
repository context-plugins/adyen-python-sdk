<!-- Generated file — do not edit; regenerated with the SDK. -->

# ApiCredentialsMerchantLevel — operations

Accessor: `client.api_credentials_merchant_level` · Source: `adyen/apis/api_credentials_merchant_level.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api_credentials_merchant_level.get_merchants_merchant_id_api_credentials

- **Route**: `GET /merchants/{merchantId}/apiCredentials`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_api_credentials(merchant_id: str, *, page_number: int | None = None, page_size: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize`
- **Returns (parsed)**: `ListMerchantApiCredentialsResponse`
- **Returns (raw)**: `ApiResult[ListMerchantApiCredentialsResponse, GetMerchantsMerchantIdApiCredentialsErrorBody]`
- **Error**: `GetMerchantsMerchantIdApiCredentialsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListMerchantApiCredentialsResponse` | `adyen/models/list_merchant_api_credentials_response.py` |
| `GetMerchantsMerchantIdApiCredentialsErrorBody` | `adyen/errors/get_merchants_merchant_id_api_credentials_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.api_credentials_merchant_level.get_merchants_merchant_id_api_credentials_api_credential_id

- **Route**: `GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_api_credentials_api_credential_id(merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `api_credential_id`
- **Params**: `merchant_id` — path `merchantId` · `api_credential_id` — path `apiCredentialId`
- **Returns (parsed)**: `ApiCredential`
- **Returns (raw)**: `ApiResult[ApiCredential, GetMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody]`
- **Error**: `GetMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiCredential` | `adyen/models/api_credential.py` |
| `GetMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody` | `adyen/errors/get_merchants_merchant_id_api_credentials_api_credential_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.api_credentials_merchant_level.patch_merchants_merchant_id_api_credentials_api_credential_id

- **Route**: `PATCH /merchants/{merchantId}/apiCredentials/{apiCredentialId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_api_credentials_api_credential_id(merchant_id: str, api_credential_id: str, *, body: UpdateMerchantApiCredentialRequest | UpdateMerchantApiCredentialRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `api_credential_id`
- **Params**: `merchant_id` — path `merchantId` · `api_credential_id` — path `apiCredentialId` · `body` — JSON body
- **Returns (parsed)**: `ApiCredential`
- **Returns (raw)**: `ApiResult[ApiCredential, PatchMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody]`
- **Error**: `PatchMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateMerchantApiCredentialRequest` | `adyen/models/update_merchant_api_credential_request.py` |
| `UpdateMerchantApiCredentialRequestDict` | `adyen/models/update_merchant_api_credential_request.py` |
| `ApiCredential` | `adyen/models/api_credential.py` |
| `PatchMerchantsMerchantIdApiCredentialsApiCredentialIdErrorBody` | `adyen/errors/patch_merchants_merchant_id_api_credentials_api_credential_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.api_credentials_merchant_level.post_merchants_merchant_id_api_credentials

- **Route**: `POST /merchants/{merchantId}/apiCredentials`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_api_credentials(merchant_id: str, *, body: CreateMerchantApiCredentialRequest | CreateMerchantApiCredentialRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `body` — JSON body
- **Returns (parsed)**: `CreateApiCredentialResponse`
- **Returns (raw)**: `ApiResult[CreateApiCredentialResponse, PostMerchantsMerchantIdApiCredentialsErrorBody]`
- **Error**: `PostMerchantsMerchantIdApiCredentialsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateMerchantApiCredentialRequest` | `adyen/models/create_merchant_api_credential_request.py` |
| `CreateMerchantApiCredentialRequestDict` | `adyen/models/create_merchant_api_credential_request.py` |
| `CreateApiCredentialResponse` | `adyen/models/create_api_credential_response.py` |
| `PostMerchantsMerchantIdApiCredentialsErrorBody` | `adyen/errors/post_merchants_merchant_id_api_credentials_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

