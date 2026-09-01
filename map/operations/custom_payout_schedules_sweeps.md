<!-- Generated file — do not edit; regenerated with the SDK. -->

# CustomPayoutSchedulesSweeps — operations

Accessor: `client.custom_payout_schedules_sweeps` · Source: `adyen/apis/custom_payout_schedules_sweeps.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.custom_payout_schedules_sweeps.delete_balance_accounts_balance_account_id_sweeps_sweep_id

- **Route**: `DELETE /balanceAccounts/{balanceAccountId}/sweeps/{sweepId}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def delete_balance_accounts_balance_account_id_sweeps_sweep_id(balance_account_id: str, sweep_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`, `sweep_id`
- **Params**: `balance_account_id` — path `balanceAccountId` · `sweep_id` — path `sweepId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody]`
- **Error**: `DeleteBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody` | `adyen/errors/delete_balance_accounts_balance_account_id_sweeps_sweep_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.custom_payout_schedules_sweeps.get_balance_accounts_balance_account_id_sweeps

- **Route**: `GET /balanceAccounts/{balanceAccountId}/sweeps`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_balance_accounts_balance_account_id_sweeps(balance_account_id: str, *, offset: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`
- **Params**: `balance_account_id` — path `balanceAccountId` · `offset` — query · `limit` — query
- **Returns (parsed)**: `BalanceSweepConfigurationsResponse`
- **Returns (raw)**: `ApiResult[BalanceSweepConfigurationsResponse, GetBalanceAccountsBalanceAccountIdSweepsErrorBody]`
- **Error**: `GetBalanceAccountsBalanceAccountIdSweepsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceSweepConfigurationsResponse` | `adyen/models/balance_sweep_configurations_response.py` |
| `GetBalanceAccountsBalanceAccountIdSweepsErrorBody` | `adyen/errors/get_balance_accounts_balance_account_id_sweeps_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.custom_payout_schedules_sweeps.get_balance_accounts_balance_account_id_sweeps_sweep_id

- **Route**: `GET /balanceAccounts/{balanceAccountId}/sweeps/{sweepId}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_balance_accounts_balance_account_id_sweeps_sweep_id(balance_account_id: str, sweep_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`, `sweep_id`
- **Params**: `balance_account_id` — path `balanceAccountId` · `sweep_id` — path `sweepId`
- **Returns (parsed)**: `SweepConfigurationV2`
- **Returns (raw)**: `ApiResult[SweepConfigurationV2, GetBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody]`
- **Error**: `GetBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SweepConfigurationV2` | `adyen/models/sweep_configuration_v2.py` |
| `GetBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody` | `adyen/errors/get_balance_accounts_balance_account_id_sweeps_sweep_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.custom_payout_schedules_sweeps.patch_balance_accounts_balance_account_id_sweeps_sweep_id

- **Route**: `PATCH /balanceAccounts/{balanceAccountId}/sweeps/{sweepId}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def patch_balance_accounts_balance_account_id_sweeps_sweep_id(balance_account_id: str, sweep_id: str, *, body: UpdateSweepConfigurationV2 | UpdateSweepConfigurationV2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`, `sweep_id`
- **Params**: `balance_account_id` — path `balanceAccountId` · `sweep_id` — path `sweepId` · `body` — JSON body
- **Returns (parsed)**: `SweepConfigurationV2`
- **Returns (raw)**: `ApiResult[SweepConfigurationV2, PatchBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody]`
- **Error**: `PatchBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateSweepConfigurationV2` | `adyen/models/update_sweep_configuration_v2.py` |
| `UpdateSweepConfigurationV2Dict` | `adyen/models/update_sweep_configuration_v2.py` |
| `SweepConfigurationV2` | `adyen/models/sweep_configuration_v2.py` |
| `PatchBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody` | `adyen/errors/patch_balance_accounts_balance_account_id_sweeps_sweep_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.custom_payout_schedules_sweeps.post_balance_accounts_balance_account_id_sweeps

- **Route**: `POST /balanceAccounts/{balanceAccountId}/sweeps`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_balance_accounts_balance_account_id_sweeps(balance_account_id: str, *, body: CreateSweepConfigurationV2 | CreateSweepConfigurationV2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`
- **Params**: `balance_account_id` — path `balanceAccountId` · `body` — JSON body
- **Returns (parsed)**: `SweepConfigurationV2`
- **Returns (raw)**: `ApiResult[SweepConfigurationV2, PostBalanceAccountsBalanceAccountIdSweepsErrorBody]`
- **Error**: `PostBalanceAccountsBalanceAccountIdSweepsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateSweepConfigurationV2` | `adyen/models/create_sweep_configuration_v2.py` |
| `CreateSweepConfigurationV2Dict` | `adyen/models/create_sweep_configuration_v2.py` |
| `SweepConfigurationV2` | `adyen/models/sweep_configuration_v2.py` |
| `PostBalanceAccountsBalanceAccountIdSweepsErrorBody` | `adyen/errors/post_balance_accounts_balance_account_id_sweeps_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

