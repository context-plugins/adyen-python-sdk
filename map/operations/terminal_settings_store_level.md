<!-- Generated file — do not edit; regenerated with the SDK. -->

# TerminalSettingsStoreLevel — operations

Accessor: `client.terminal_settings_store_level` · Source: `adyen/apis/terminal_settings_store_level.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.terminal_settings_store_level.get_merchants_merchant_id_stores_reference_terminal_logos

- **Route**: `GET /merchants/{merchantId}/stores/{reference}/terminalLogos`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_stores_reference_terminal_logos(merchant_id: str, reference: str, model: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `reference`, `model`
- **Params**: `merchant_id` — path `merchantId` · `reference` — path · `model` — query
- **Returns (parsed)**: `Logo`
- **Returns (raw)**: `ApiResult[Logo, GetMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody]`
- **Error**: `GetMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Logo` | `adyen/models/logo.py` |
| `GetMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody` | `adyen/errors/get_merchants_merchant_id_stores_reference_terminal_logos_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_store_level.get_merchants_merchant_id_stores_reference_terminal_settings

- **Route**: `GET /merchants/{merchantId}/stores/{reference}/terminalSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_merchants_merchant_id_stores_reference_terminal_settings(merchant_id: str, reference: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `reference`
- **Params**: `merchant_id` — path `merchantId` · `reference` — path
- **Returns (parsed)**: `TerminalSettings`
- **Returns (raw)**: `ApiResult[TerminalSettings, GetMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody]`
- **Error**: `GetMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalSettings` | `adyen/models/terminal_settings.py` |
| `GetMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody` | `adyen/errors/get_merchants_merchant_id_stores_reference_terminal_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_store_level.get_stores_store_id_terminal_logos

- **Route**: `GET /stores/{storeId}/terminalLogos`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_stores_store_id_terminal_logos(store_id: str, model: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `store_id`, `model`
- **Params**: `store_id` — path `storeId` · `model` — query
- **Returns (parsed)**: `Logo`
- **Returns (raw)**: `ApiResult[Logo, GetStoresStoreIdTerminalLogosErrorBody]`
- **Error**: `GetStoresStoreIdTerminalLogosErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Logo` | `adyen/models/logo.py` |
| `GetStoresStoreIdTerminalLogosErrorBody` | `adyen/errors/get_stores_store_id_terminal_logos_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_store_level.get_stores_store_id_terminal_settings

- **Route**: `GET /stores/{storeId}/terminalSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_stores_store_id_terminal_settings(store_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `store_id`
- **Params**: `store_id` — path `storeId`
- **Returns (parsed)**: `TerminalSettings`
- **Returns (raw)**: `ApiResult[TerminalSettings, GetStoresStoreIdTerminalSettingsErrorBody]`
- **Error**: `GetStoresStoreIdTerminalSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalSettings` | `adyen/models/terminal_settings.py` |
| `GetStoresStoreIdTerminalSettingsErrorBody` | `adyen/errors/get_stores_store_id_terminal_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_store_level.patch_merchants_merchant_id_stores_reference_terminal_logos

- **Route**: `PATCH /merchants/{merchantId}/stores/{reference}/terminalLogos`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_stores_reference_terminal_logos(merchant_id: str, reference: str, model: str, *, body: Logo | LogoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `reference`, `model`
- **Params**: `merchant_id` — path `merchantId` · `reference` — path · `model` — query · `body` — JSON body
- **Returns (parsed)**: `Logo`
- **Returns (raw)**: `ApiResult[Logo, PatchMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody]`
- **Error**: `PatchMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Logo` | `adyen/models/logo.py` |
| `LogoDict` | `adyen/models/logo.py` |
| `PatchMerchantsMerchantIdStoresReferenceTerminalLogosErrorBody` | `adyen/errors/patch_merchants_merchant_id_stores_reference_terminal_logos_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_store_level.patch_merchants_merchant_id_stores_reference_terminal_settings

- **Route**: `PATCH /merchants/{merchantId}/stores/{reference}/terminalSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_merchants_merchant_id_stores_reference_terminal_settings(merchant_id: str, reference: str, *, body: TerminalSettings | TerminalSettingsDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `reference`
- **Params**: `merchant_id` — path `merchantId` · `reference` — path · `body` — JSON body
- **Returns (parsed)**: `TerminalSettings`
- **Returns (raw)**: `ApiResult[TerminalSettings, PatchMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody]`
- **Error**: `PatchMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalSettings` | `adyen/models/terminal_settings.py` |
| `TerminalSettingsDict` | `adyen/models/terminal_settings.py` |
| `PatchMerchantsMerchantIdStoresReferenceTerminalSettingsErrorBody` | `adyen/errors/patch_merchants_merchant_id_stores_reference_terminal_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_store_level.patch_stores_store_id_terminal_logos

- **Route**: `PATCH /stores/{storeId}/terminalLogos`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_stores_store_id_terminal_logos(store_id: str, model: str, *, body: Logo | LogoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `store_id`, `model`
- **Params**: `store_id` — path `storeId` · `model` — query · `body` — JSON body
- **Returns (parsed)**: `Logo`
- **Returns (raw)**: `ApiResult[Logo, PatchStoresStoreIdTerminalLogosErrorBody]`
- **Error**: `PatchStoresStoreIdTerminalLogosErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Logo` | `adyen/models/logo.py` |
| `LogoDict` | `adyen/models/logo.py` |
| `PatchStoresStoreIdTerminalLogosErrorBody` | `adyen/errors/patch_stores_store_id_terminal_logos_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_store_level.patch_stores_store_id_terminal_settings

- **Route**: `PATCH /stores/{storeId}/terminalSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_stores_store_id_terminal_settings(store_id: str, *, body: TerminalSettings | TerminalSettingsDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `store_id`
- **Params**: `store_id` — path `storeId` · `body` — JSON body
- **Returns (parsed)**: `TerminalSettings`
- **Returns (raw)**: `ApiResult[TerminalSettings, PatchStoresStoreIdTerminalSettingsErrorBody]`
- **Error**: `PatchStoresStoreIdTerminalSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalSettings` | `adyen/models/terminal_settings.py` |
| `TerminalSettingsDict` | `adyen/models/terminal_settings.py` |
| `PatchStoresStoreIdTerminalSettingsErrorBody` | `adyen/errors/patch_stores_store_id_terminal_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

