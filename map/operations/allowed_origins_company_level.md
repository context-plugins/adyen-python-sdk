<!-- Generated file — do not edit; regenerated with the SDK. -->

# AllowedOriginsCompanyLevel — operations

Accessor: `client.allowed_origins_company_level` · Source: `adyen/apis/allowed_origins_company_level.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.allowed_origins_company_level.delete_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id

- **Route**: `DELETE /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def delete_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id(company_id: str, api_credential_id: str, origin_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `api_credential_id`, `origin_id`
- **Params**: `company_id` — path `companyId` · `api_credential_id` — path `apiCredentialId` · `origin_id` — path `originId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody]`
- **Error**: `DeleteCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody` | `adyen/errors/delete_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.allowed_origins_company_level.get_companies_company_id_api_credentials_api_credential_id_allowed_origins

- **Route**: `GET /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_api_credentials_api_credential_id_allowed_origins(company_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `api_credential_id`
- **Params**: `company_id` — path `companyId` · `api_credential_id` — path `apiCredentialId`
- **Returns (parsed)**: `AllowedOriginsResponse`
- **Returns (raw)**: `ApiResult[AllowedOriginsResponse, GetCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody]`
- **Error**: `GetCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AllowedOriginsResponse` | `adyen/models/allowed_origins_response.py` |
| `GetCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody` | `adyen/errors/get_companies_company_id_api_credentials_api_credential_id_allowed_origins_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.allowed_origins_company_level.get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id

- **Route**: `GET /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id(company_id: str, api_credential_id: str, origin_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `api_credential_id`, `origin_id`
- **Params**: `company_id` — path `companyId` · `api_credential_id` — path `apiCredentialId` · `origin_id` — path `originId`
- **Returns (parsed)**: `AllowedOrigin`
- **Returns (raw)**: `ApiResult[AllowedOrigin, GetCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody]`
- **Error**: `GetCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AllowedOrigin` | `adyen/models/allowed_origin.py` |
| `GetCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginIdErrorBody` | `adyen/errors/get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.allowed_origins_company_level.post_companies_company_id_api_credentials_api_credential_id_allowed_origins

- **Route**: `POST /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_api_credentials_api_credential_id_allowed_origins(company_id: str, api_credential_id: str, *, body: AllowedOrigin | AllowedOriginDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `api_credential_id`
- **Params**: `company_id` — path `companyId` · `api_credential_id` — path `apiCredentialId` · `body` — JSON body
- **Returns (parsed)**: `AllowedOrigin`
- **Returns (raw)**: `ApiResult[AllowedOrigin, PostCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody]`
- **Error**: `PostCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AllowedOrigin` | `adyen/models/allowed_origin.py` |
| `AllowedOriginDict` | `adyen/models/allowed_origin.py` |
| `PostCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsErrorBody` | `adyen/errors/post_companies_company_id_api_credentials_api_credential_id_allowed_origins_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

