<!-- Generated file — do not edit; regenerated with the SDK. -->

# TerminalActionsCompanyLevel — operations

Accessor: `client.terminal_actions_company_level` · Source: `adyen/apis/terminal_actions_company_level.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.terminal_actions_company_level.get_companies_company_id_terminal_actions

- **Route**: `GET /companies/{companyId}/terminalActions`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_terminal_actions(company_id: str, *, page_number: int | None = None, page_size: int | None = None, status: str | None = None, type_: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`
- **Params**: `company_id` — path `companyId` · `page_number` — query `pageNumber` · `page_size` — query `pageSize` · `status` — query · `type_` — query `type`
- **Returns (parsed)**: `ListExternalTerminalActionsResponse`
- **Returns (raw)**: `ApiResult[ListExternalTerminalActionsResponse, GetCompaniesCompanyIdTerminalActionsErrorBody]`
- **Error**: `GetCompaniesCompanyIdTerminalActionsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListExternalTerminalActionsResponse` | `adyen/models/list_external_terminal_actions_response.py` |
| `GetCompaniesCompanyIdTerminalActionsErrorBody` | `adyen/errors/get_companies_company_id_terminal_actions_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.terminal_actions_company_level.get_companies_company_id_terminal_actions_action_id

- **Route**: `GET /companies/{companyId}/terminalActions/{actionId}`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def get_companies_company_id_terminal_actions_action_id(company_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `company_id`, `action_id`
- **Params**: `company_id` — path `companyId` · `action_id` — path `actionId`
- **Returns (parsed)**: `ExternalTerminalAction`
- **Returns (raw)**: `ApiResult[ExternalTerminalAction, GetCompaniesCompanyIdTerminalActionsActionIdErrorBody]`
- **Error**: `GetCompaniesCompanyIdTerminalActionsActionIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ExternalTerminalAction` | `adyen/models/external_terminal_action.py` |
| `GetCompaniesCompanyIdTerminalActionsActionIdErrorBody` | `adyen/errors/get_companies_company_id_terminal_actions_action_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

