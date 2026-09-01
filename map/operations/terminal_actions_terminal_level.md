<!-- Generated file — do not edit; regenerated with the SDK. -->

# TerminalActionsTerminalLevel — operations

Accessor: `client.terminal_actions_terminal_level` · Source: `adyen/apis/terminal_actions_terminal_level.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.terminal_actions_terminal_level.post_terminals_schedule_actions

- **Route**: `POST /terminals/scheduleActions`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default9`
- **Signature**: `def post_terminals_schedule_actions(*, body: ScheduleTerminalActionsRequest | ScheduleTerminalActionsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ScheduleTerminalActionsResponse`
- **Returns (raw)**: `ApiResult[ScheduleTerminalActionsResponse, PostTerminalsScheduleActionsErrorBody]`
- **Error**: `PostTerminalsScheduleActionsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ScheduleTerminalActionsRequest` | `adyen/models/schedule_terminal_actions_request.py` |
| `ScheduleTerminalActionsRequestDict` | `adyen/models/schedule_terminal_actions_request.py` |
| `ScheduleTerminalActionsResponse` | `adyen/models/schedule_terminal_actions_response.py` |
| `PostTerminalsScheduleActionsErrorBody` | `adyen/errors/post_terminals_schedule_actions_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

