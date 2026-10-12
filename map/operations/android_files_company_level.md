<!-- Generated file — do not edit; regenerated with the SDK. -->

# AndroidFilesCompanyLevel — operations

Accessor: `client.android_files_company_level` · Source: `adyen/apis/android_files_company_level.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.android_files_company_level.get_companies_company_id_android_apps

- **Route**: `GET /companies/{companyId}/androidApps`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_android_apps(company_id: str, *, page_number: int | None = None, page_size: int | None = None, package_name: str | None = None, version_code: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize` · `package_name` — query `packageName` · `version_code` — query `versionCode`
- **Returns (parsed)**: `AndroidAppsResponse`
- **Returns (raw)**: `ApiResult[AndroidAppsResponse, GetCompaniesCompanyIdAndroidAppsErrorBody]`
- **Error**: `GetCompaniesCompanyIdAndroidAppsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AndroidAppsResponse` | `adyen/models/android_apps_response.py` |
| `GetCompaniesCompanyIdAndroidAppsErrorBody` | `adyen/errors/get_companies_company_id_android_apps_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.android_files_company_level.get_companies_company_id_android_apps_id

- **Route**: `GET /companies/{companyId}/androidApps/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_android_apps_id(company_id: str, id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `id_`
- **Params**: `company_id` — path `companyId` · `id_` — path `id`
- **Returns (parsed)**: `AndroidApp`
- **Returns (raw)**: `ApiResult[AndroidApp, GetCompaniesCompanyIdAndroidAppsIdErrorBody]`
- **Error**: `GetCompaniesCompanyIdAndroidAppsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AndroidApp` | `adyen/models/android_app.py` |
| `GetCompaniesCompanyIdAndroidAppsIdErrorBody` | `adyen/errors/get_companies_company_id_android_apps_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.android_files_company_level.get_companies_company_id_android_certificates

- **Route**: `GET /companies/{companyId}/androidCertificates`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_android_certificates(company_id: str, *, page_number: int | None = None, page_size: int | None = None, certificate_name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize` · `certificate_name` — query `certificateName`
- **Returns (parsed)**: `AndroidCertificatesResponse`
- **Returns (raw)**: `ApiResult[AndroidCertificatesResponse, GetCompaniesCompanyIdAndroidCertificatesErrorBody]`
- **Error**: `GetCompaniesCompanyIdAndroidCertificatesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AndroidCertificatesResponse` | `adyen/models/android_certificates_response.py` |
| `GetCompaniesCompanyIdAndroidCertificatesErrorBody` | `adyen/errors/get_companies_company_id_android_certificates_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.android_files_company_level.patch_companies_company_id_android_apps_id

- **Route**: `PATCH /companies/{companyId}/androidApps/{id}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_companies_company_id_android_apps_id(company_id: str, id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `id_`
- **Params**: `company_id` — path `companyId` · `id_` — path `id`
- **Returns (parsed)**: `ReprocessAndroidAppResponse`
- **Returns (raw)**: `ApiResult[ReprocessAndroidAppResponse, PatchCompaniesCompanyIdAndroidAppsIdErrorBody]`
- **Error**: `PatchCompaniesCompanyIdAndroidAppsIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ReprocessAndroidAppResponse` | `adyen/models/reprocess_android_app_response.py` |
| `PatchCompaniesCompanyIdAndroidAppsIdErrorBody` | `adyen/errors/patch_companies_company_id_android_apps_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.android_files_company_level.post_companies_company_id_android_apps

- **Route**: `POST /companies/{companyId}/androidApps`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_android_apps(company_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId`
- **Returns (parsed)**: `UploadAndroidAppResponse`
- **Returns (raw)**: `ApiResult[UploadAndroidAppResponse, PostCompaniesCompanyIdAndroidAppsErrorBody]`
- **Error**: `PostCompaniesCompanyIdAndroidAppsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UploadAndroidAppResponse` | `adyen/models/upload_android_app_response.py` |
| `PostCompaniesCompanyIdAndroidAppsErrorBody` | `adyen/errors/post_companies_company_id_android_apps_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.android_files_company_level.post_companies_company_id_android_certificates

- **Route**: `POST /companies/{companyId}/androidCertificates`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_companies_company_id_android_certificates(company_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId`
- **Returns (parsed)**: `UploadAndroidCertificateResponse`
- **Returns (raw)**: `ApiResult[UploadAndroidCertificateResponse, PostCompaniesCompanyIdAndroidCertificatesErrorBody]`
- **Error**: `PostCompaniesCompanyIdAndroidCertificatesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UploadAndroidCertificateResponse` | `adyen/models/upload_android_certificate_response.py` |
| `PostCompaniesCompanyIdAndroidCertificatesErrorBody` | `adyen/errors/post_companies_company_id_android_certificates_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

