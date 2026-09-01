<!-- Generated file — do not edit; regenerated with the SDK. -->

# ClientKeyCompanyLevel — operations

Accessor: `client.client_key_company_level` · Source: `adyen/apis/client_key_company_level.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.client_key_company_level.post_companies_company_id_api_credentials_api_credential_id_generate_client_key

- **Route**: `POST /companies/{companyId}/apiCredentials/{apiCredentialId}/generateClientKey`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_api_credentials_api_credential_id_generate_client_key(company_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `api_credential_id`
- **Params**: `company_id` — path `companyId` · `api_credential_id` — path `apiCredentialId`
- **Returns (parsed)**: `GenerateClientKeyResponse`
- **Returns (raw)**: `ApiResult[GenerateClientKeyResponse, PostCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKeyErrorBody]`
- **Error**: `PostCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKeyErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateClientKeyResponse` | `adyen/models/generate_client_key_response.py` |
| `PostCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKeyErrorBody` | `adyen/errors/post_companies_company_id_api_credentials_api_credential_id_generate_client_key_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

