<!-- Generated file — do not edit; regenerated with the SDK. -->

# TerminalSettingsTerminalLevel — operations

Accessor: `client.terminal_settings_terminal_level` · Source: `adyen/apis/terminal_settings_terminal_level.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.terminal_settings_terminal_level.get_terminals_terminal_id_terminal_logos

- **Route**: `GET /terminals/{terminalId}/terminalLogos`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_terminals_terminal_id_terminal_logos(terminal_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `terminal_id`
- **Params**: `terminal_id` — path `terminalId`
- **Returns (parsed)**: `Logo`
- **Returns (raw)**: `ApiResult[Logo, GetTerminalsTerminalIdTerminalLogosErrorBody]`
- **Error**: `GetTerminalsTerminalIdTerminalLogosErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Logo` | `adyen/models/logo.py` |
| `GetTerminalsTerminalIdTerminalLogosErrorBody` | `adyen/errors/get_terminals_terminal_id_terminal_logos_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_terminal_level.get_terminals_terminal_id_terminal_settings

- **Route**: `GET /terminals/{terminalId}/terminalSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_terminals_terminal_id_terminal_settings(terminal_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `terminal_id`
- **Params**: `terminal_id` — path `terminalId`
- **Returns (parsed)**: `TerminalSettings`
- **Returns (raw)**: `ApiResult[TerminalSettings, GetTerminalsTerminalIdTerminalSettingsErrorBody]`
- **Error**: `GetTerminalsTerminalIdTerminalSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalSettings` | `adyen/models/terminal_settings.py` |
| `GetTerminalsTerminalIdTerminalSettingsErrorBody` | `adyen/errors/get_terminals_terminal_id_terminal_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_terminal_level.patch_terminals_terminal_id_terminal_logos

- **Route**: `PATCH /terminals/{terminalId}/terminalLogos`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_terminals_terminal_id_terminal_logos(terminal_id: str, *, body: Logo | LogoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `terminal_id`
- **Params**: `terminal_id` — path `terminalId` · `body` — JSON body
- **Returns (parsed)**: `Logo`
- **Returns (raw)**: `ApiResult[Logo, PatchTerminalsTerminalIdTerminalLogosErrorBody]`
- **Error**: `PatchTerminalsTerminalIdTerminalLogosErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Logo` | `adyen/models/logo.py` |
| `LogoDict` | `adyen/models/logo.py` |
| `PatchTerminalsTerminalIdTerminalLogosErrorBody` | `adyen/errors/patch_terminals_terminal_id_terminal_logos_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_settings_terminal_level.patch_terminals_terminal_id_terminal_settings

- **Route**: `PATCH /terminals/{terminalId}/terminalSettings`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def patch_terminals_terminal_id_terminal_settings(terminal_id: str, *, body: TerminalSettings | TerminalSettingsDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `terminal_id`
- **Params**: `terminal_id` — path `terminalId` · `body` — JSON body
- **Returns (parsed)**: `TerminalSettings`
- **Returns (raw)**: `ApiResult[TerminalSettings, PatchTerminalsTerminalIdTerminalSettingsErrorBody]`
- **Error**: `PatchTerminalsTerminalIdTerminalSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TerminalSettings` | `adyen/models/terminal_settings.py` |
| `TerminalSettingsDict` | `adyen/models/terminal_settings.py` |
| `PatchTerminalsTerminalIdTerminalSettingsErrorBody` | `adyen/errors/patch_terminals_terminal_id_terminal_settings_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

