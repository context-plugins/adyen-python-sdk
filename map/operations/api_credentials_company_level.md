<!-- Generated file — do not edit; regenerated with the SDK. -->

# ApiCredentialsCompanyLevel — operations

Accessor: `client.api_credentials_company_level` · Source: `adyen/apis/api_credentials_company_level.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api_credentials_company_level.get_companies_company_id_api_credentials

- **Route**: `GET /companies/{companyId}/apiCredentials`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_api_credentials(company_id: str, *, page_number: int | None = None, page_size: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize`
- **Returns (parsed)**: `ListCompanyApiCredentialsResponse`
- **Returns (raw)**: `ApiResult[ListCompanyApiCredentialsResponse, GetCompaniesCompanyIdApiCredentialsErrorBody]`
- **Error**: `GetCompaniesCompanyIdApiCredentialsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListCompanyApiCredentialsResponse` | `adyen/models/list_company_api_credentials_response.py` |
| `GetCompaniesCompanyIdApiCredentialsErrorBody` | `adyen/errors/get_companies_company_id_api_credentials_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.api_credentials_company_level.get_companies_company_id_api_credentials_api_credential_id

- **Route**: `GET /companies/{companyId}/apiCredentials/{apiCredentialId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_api_credentials_api_credential_id(company_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `api_credential_id`
- **Params**: `company_id` — path `companyId` · `api_credential_id` — path `apiCredentialId`
- **Returns (parsed)**: `CompanyApiCredential`
- **Returns (raw)**: `ApiResult[CompanyApiCredential, GetCompaniesCompanyIdApiCredentialsApiCredentialIdErrorBody]`
- **Error**: `GetCompaniesCompanyIdApiCredentialsApiCredentialIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CompanyApiCredential` | `adyen/models/company_api_credential.py` |
| `GetCompaniesCompanyIdApiCredentialsApiCredentialIdErrorBody` | `adyen/errors/get_companies_company_id_api_credentials_api_credential_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.api_credentials_company_level.patch_companies_company_id_api_credentials_api_credential_id

- **Route**: `PATCH /companies/{companyId}/apiCredentials/{apiCredentialId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_companies_company_id_api_credentials_api_credential_id(company_id: str, api_credential_id: str, *, body: UpdateCompanyApiCredentialRequest | UpdateCompanyApiCredentialRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `api_credential_id`
- **Params**: `company_id` — path `companyId` · `api_credential_id` — path `apiCredentialId` · `body` — JSON body
- **Returns (parsed)**: `CompanyApiCredential`
- **Returns (raw)**: `ApiResult[CompanyApiCredential, PatchCompaniesCompanyIdApiCredentialsApiCredentialIdErrorBody]`
- **Error**: `PatchCompaniesCompanyIdApiCredentialsApiCredentialIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateCompanyApiCredentialRequest` | `adyen/models/update_company_api_credential_request.py` |
| `UpdateCompanyApiCredentialRequestDict` | `adyen/models/update_company_api_credential_request.py` |
| `CompanyApiCredential` | `adyen/models/company_api_credential.py` |
| `PatchCompaniesCompanyIdApiCredentialsApiCredentialIdErrorBody` | `adyen/errors/patch_companies_company_id_api_credentials_api_credential_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.api_credentials_company_level.post_companies_company_id_api_credentials

- **Route**: `POST /companies/{companyId}/apiCredentials`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_api_credentials(company_id: str, *, body: CreateCompanyApiCredentialRequest | CreateCompanyApiCredentialRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `body` — JSON body
- **Returns (parsed)**: `CreateCompanyApiCredentialResponse`
- **Returns (raw)**: `ApiResult[CreateCompanyApiCredentialResponse, PostCompaniesCompanyIdApiCredentialsErrorBody]`
- **Error**: `PostCompaniesCompanyIdApiCredentialsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateCompanyApiCredentialRequest` | `adyen/models/create_company_api_credential_request.py` |
| `CreateCompanyApiCredentialRequestDict` | `adyen/models/create_company_api_credential_request.py` |
| `CreateCompanyApiCredentialResponse` | `adyen/models/create_company_api_credential_response.py` |
| `PostCompaniesCompanyIdApiCredentialsErrorBody` | `adyen/errors/post_companies_company_id_api_credentials_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

