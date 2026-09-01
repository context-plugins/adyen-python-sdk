<!-- Generated file — do not edit; regenerated with the SDK. -->

# TerminalSettingsMerchantLevel — operations

Accessor: `client.terminal_settings_merchant_level` · Source: `adyen/apis/terminal_settings_merchant_level.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.terminal_settings_merchant_level.get_merchants_merchant_id_terminal_logos

- **Route**: `GET /merchants/{merchantId}/terminalLogos`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_terminal_logos(merchant_id: str, model: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `model`
- **Params**: `merchant_id` — path `merchantId` · `model` — query
- **Returns (parsed)**: `Logo`
- **Returns (raw)**: `ApiResult[Logo, GetMerchantsMerchantIdTerminalLogosErrorBody]`
- **Error**: `GetMerchantsMerchantIdTerminalLogosErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Logo` | `adyen/models/logo.py` |
| `GetMerchantsMerchantIdTerminalLogosErrorBody` | `adyen/errors/get_merchants_merchant_id_terminal_logos_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_merchant_level.get_merchants_merchant_id_terminal_settings

- **Route**: `GET /merchants/{merchantId}/terminalSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_terminal_settings(merchant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId`
- **Returns (parsed)**: `TerminalSettings`
- **Returns (raw)**: `ApiResult[TerminalSettings, GetMerchantsMerchantIdTerminalSettingsErrorBody]`
- **Error**: `GetMerchantsMerchantIdTerminalSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalSettings` | `adyen/models/terminal_settings.py` |
| `GetMerchantsMerchantIdTerminalSettingsErrorBody` | `adyen/errors/get_merchants_merchant_id_terminal_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_merchant_level.patch_merchants_merchant_id_terminal_logos

- **Route**: `PATCH /merchants/{merchantId}/terminalLogos`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_terminal_logos(merchant_id: str, model: str, *, body: Logo | LogoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `model`
- **Params**: `merchant_id` — path `merchantId` · `model` — query · `body` — JSON body
- **Returns (parsed)**: `Logo`
- **Returns (raw)**: `ApiResult[Logo, PatchMerchantsMerchantIdTerminalLogosErrorBody]`
- **Error**: `PatchMerchantsMerchantIdTerminalLogosErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Logo` | `adyen/models/logo.py` |
| `LogoDict` | `adyen/models/logo.py` |
| `PatchMerchantsMerchantIdTerminalLogosErrorBody` | `adyen/errors/patch_merchants_merchant_id_terminal_logos_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_merchant_level.patch_merchants_merchant_id_terminal_settings

- **Route**: `PATCH /merchants/{merchantId}/terminalSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_terminal_settings(merchant_id: str, *, body: TerminalSettings | TerminalSettingsDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path `merchantId` · `body` — JSON body
- **Returns (parsed)**: `TerminalSettings`
- **Returns (raw)**: `ApiResult[TerminalSettings, PatchMerchantsMerchantIdTerminalSettingsErrorBody]`
- **Error**: `PatchMerchantsMerchantIdTerminalSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalSettings` | `adyen/models/terminal_settings.py` |
| `TerminalSettingsDict` | `adyen/models/terminal_settings.py` |
| `PatchMerchantsMerchantIdTerminalSettingsErrorBody` | `adyen/errors/patch_merchants_merchant_id_terminal_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

