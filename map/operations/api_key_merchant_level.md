<!-- Generated file — do not edit; regenerated with the SDK. -->

# ApiKeyMerchantLevel — operations

Accessor: `client.api_key_merchant_level` · Source: `adyen/apis/api_key_merchant_level.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api_key_merchant_level.post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key

- **Route**: `POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key(merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `api_credential_id`
- **Params**: `merchant_id` — path `merchantId` · `api_credential_id` — path `apiCredentialId`
- **Returns (parsed)**: `GenerateApiKeyResponse`
- **Returns (raw)**: `ApiResult[GenerateApiKeyResponse, PostMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKeyErrorBody]`
- **Error**: `PostMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKeyErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateApiKeyResponse` | `adyen/models/generate_api_key_response.py` |
| `PostMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKeyErrorBody` | `adyen/errors/post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

