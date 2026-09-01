<!-- Generated file — do not edit; regenerated with the SDK. -->

# TerminalSettingsCompanyLevel — operations

Accessor: `client.terminal_settings_company_level` · Source: `adyen/apis/terminal_settings_company_level.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.terminal_settings_company_level.get_companies_company_id_terminal_logos

- **Route**: `GET /companies/{companyId}/terminalLogos`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_terminal_logos(company_id: str, model: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `model`
- **Params**: `company_id` — path `companyId` · `model` — query
- **Returns (parsed)**: `Logo`
- **Returns (raw)**: `ApiResult[Logo, GetCompaniesCompanyIdTerminalLogosErrorBody]`
- **Error**: `GetCompaniesCompanyIdTerminalLogosErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Logo` | `adyen/models/logo.py` |
| `GetCompaniesCompanyIdTerminalLogosErrorBody` | `adyen/errors/get_companies_company_id_terminal_logos_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_company_level.get_companies_company_id_terminal_settings

- **Route**: `GET /companies/{companyId}/terminalSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_terminal_settings(company_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId`
- **Returns (parsed)**: `TerminalSettings`
- **Returns (raw)**: `ApiResult[TerminalSettings, GetCompaniesCompanyIdTerminalSettingsErrorBody]`
- **Error**: `GetCompaniesCompanyIdTerminalSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalSettings` | `adyen/models/terminal_settings.py` |
| `GetCompaniesCompanyIdTerminalSettingsErrorBody` | `adyen/errors/get_companies_company_id_terminal_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_company_level.patch_companies_company_id_terminal_logos

- **Route**: `PATCH /companies/{companyId}/terminalLogos`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_companies_company_id_terminal_logos(company_id: str, model: str, *, body: Logo | LogoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `model`
- **Params**: `company_id` — path `companyId` · `model` — query · `body` — JSON body
- **Returns (parsed)**: `Logo`
- **Returns (raw)**: `ApiResult[Logo, PatchCompaniesCompanyIdTerminalLogosErrorBody]`
- **Error**: `PatchCompaniesCompanyIdTerminalLogosErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Logo` | `adyen/models/logo.py` |
| `LogoDict` | `adyen/models/logo.py` |
| `PatchCompaniesCompanyIdTerminalLogosErrorBody` | `adyen/errors/patch_companies_company_id_terminal_logos_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_company_level.patch_companies_company_id_terminal_settings

- **Route**: `PATCH /companies/{companyId}/terminalSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_companies_company_id_terminal_settings(company_id: str, *, body: TerminalSettings | TerminalSettingsDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `body` — JSON body
- **Returns (parsed)**: `TerminalSettings`
- **Returns (raw)**: `ApiResult[TerminalSettings, PatchCompaniesCompanyIdTerminalSettingsErrorBody]`
- **Error**: `PatchCompaniesCompanyIdTerminalSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalSettings` | `adyen/models/terminal_settings.py` |
| `TerminalSettingsDict` | `adyen/models/terminal_settings.py` |
| `PatchCompaniesCompanyIdTerminalSettingsErrorBody` | `adyen/errors/patch_companies_company_id_terminal_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

