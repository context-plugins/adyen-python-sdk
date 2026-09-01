<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManagedPayoutSchedules — operations

Accessor: `client.managed_payout_schedules` · Source: `adyen/apis/managed_payout_schedules.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.managed_payout_schedules.delete_balance_accounts_balance_account_id_payout_schedules_id

- **Route**: `DELETE /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}`
- **Server**: `default13`
- **Signature**: `def delete_balance_accounts_balance_account_id_payout_schedules_id(balance_account_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`, `id`
- **Params**: `balance_account_id` — path `balanceAccountId` · `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody]`
- **Error**: `DeleteBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody` | `adyen/errors/delete_balance_accounts_balance_account_id_payout_schedules_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.managed_payout_schedules.get_balance_accounts_balance_account_id_payout_schedules

- **Route**: `GET /balanceAccounts/{balanceAccountId}/payoutSchedules`
- **Server**: `default13`
- **Signature**: `def get_balance_accounts_balance_account_id_payout_schedules(balance_account_id: str, *, currency: str | None = None, cursor: str | None = None, limit: int | None = 10, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`
- **Params**: `balance_account_id` — path `balanceAccountId` · `currency` — query · `cursor` — query · `limit` — query
- **Returns (parsed)**: `BalanceAccountConfigurations`
- **Returns (raw)**: `ApiResult[BalanceAccountConfigurations, GetBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody]`
- **Error**: `GetBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceAccountConfigurations` | `adyen/models/balance_account_configurations.py` |
| `GetBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody` | `adyen/errors/get_balance_accounts_balance_account_id_payout_schedules_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.managed_payout_schedules.get_balance_accounts_balance_account_id_payout_schedules_id

- **Route**: `GET /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}`
- **Server**: `default13`
- **Signature**: `def get_balance_accounts_balance_account_id_payout_schedules_id(balance_account_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`, `id`
- **Params**: `balance_account_id` — path `balanceAccountId` · `id` — path
- **Returns (parsed)**: `BalanceAccountConfiguration`
- **Returns (raw)**: `ApiResult[BalanceAccountConfiguration, GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody]`
- **Error**: `GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceAccountConfiguration` | `adyen/models/balance_account_configuration.py` |
| `GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody` | `adyen/errors/get_balance_accounts_balance_account_id_payout_schedules_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.managed_payout_schedules.get_balance_accounts_balance_account_id_payout_schedules_id_executions

- **Route**: `GET /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}/executions`
- **Server**: `default13`
- **Signature**: `def get_balance_accounts_balance_account_id_payout_schedules_id_executions(balance_account_id: str, id: str, offset: int, *, results: list[ExecutionResultOrStr] | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`, `id`, `offset`
- **Params**: `balance_account_id` — path `balanceAccountId` · `id` — path · `offset` — query · `results` — query · `limit` — query
- **Returns (parsed)**: `PayoutScheduleExecutions`
- **Returns (raw)**: `ApiResult[PayoutScheduleExecutions, GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdExecutionsErrorBody]`
- **Error**: `GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdExecutionsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ExecutionResultOrStr` | `adyen/models/enums/execution_result.py` |
| `PayoutScheduleExecutions` | `adyen/models/payout_schedule_executions.py` |
| `GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdExecutionsErrorBody` | `adyen/errors/get_balance_accounts_balance_account_id_payout_schedules_id_executions_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.managed_payout_schedules.get_balance_platforms_balance_platform_id_payout_schedules

- **Route**: `GET /balancePlatforms/{balancePlatformId}/payoutSchedules`
- **Server**: `default13`
- **Signature**: `def get_balance_platforms_balance_platform_id_payout_schedules(balance_platform_id: str, *, country_code: str | None = None, currency: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_platform_id`
- **Params**: `balance_platform_id` — path `balancePlatformId` · `country_code` — query `countryCode` · `currency` — query
- **Returns (parsed)**: `BalancePlatformConfigurations`
- **Returns (raw)**: `ApiResult[BalancePlatformConfigurations, GetBalancePlatformsBalancePlatformIdPayoutSchedulesErrorBody]`
- **Error**: `GetBalancePlatformsBalancePlatformIdPayoutSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalancePlatformConfigurations` | `adyen/models/balance_platform_configurations.py` |
| `GetBalancePlatformsBalancePlatformIdPayoutSchedulesErrorBody` | `adyen/errors/get_balance_platforms_balance_platform_id_payout_schedules_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.managed_payout_schedules.get_balance_platforms_balance_platform_id_payout_schedules_id

- **Route**: `GET /balancePlatforms/{balancePlatformId}/payoutSchedules/{id}`
- **Server**: `default13`
- **Signature**: `def get_balance_platforms_balance_platform_id_payout_schedules_id(balance_platform_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_platform_id`, `id`
- **Params**: `balance_platform_id` — path `balancePlatformId` · `id` — path
- **Returns (parsed)**: `BalancePlatformConfiguration`
- **Returns (raw)**: `ApiResult[BalancePlatformConfiguration, GetBalancePlatformsBalancePlatformIdPayoutSchedulesIdErrorBody]`
- **Error**: `GetBalancePlatformsBalancePlatformIdPayoutSchedulesIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalancePlatformConfiguration` | `adyen/models/balance_platform_configuration.py` |
| `GetBalancePlatformsBalancePlatformIdPayoutSchedulesIdErrorBody` | `adyen/errors/get_balance_platforms_balance_platform_id_payout_schedules_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.managed_payout_schedules.patch_balance_accounts_balance_account_id_payout_schedules_id

- **Route**: `PATCH /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}`
- **Server**: `default13`
- **Signature**: `def patch_balance_accounts_balance_account_id_payout_schedules_id(balance_account_id: str, id: str, body: BalanceAccountConfigurationUpdate | BalanceAccountConfigurationUpdateDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`, `id`, `body`
- **Params**: `balance_account_id` — path `balanceAccountId` · `id` — path · `body` — JSON body
- **Returns (parsed)**: `BalanceAccountConfiguration`
- **Returns (raw)**: `ApiResult[BalanceAccountConfiguration, PatchBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody]`
- **Error**: `PatchBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceAccountConfigurationUpdate` | `adyen/models/balance_account_configuration_update.py` |
| `BalanceAccountConfigurationUpdateDict` | `adyen/models/balance_account_configuration_update.py` |
| `BalanceAccountConfiguration` | `adyen/models/balance_account_configuration.py` |
| `PatchBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody` | `adyen/errors/patch_balance_accounts_balance_account_id_payout_schedules_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.managed_payout_schedules.post_balance_accounts_balance_account_id_payout_schedules

- **Route**: `POST /balanceAccounts/{balanceAccountId}/payoutSchedules`
- **Server**: `default13`
- **Signature**: `def post_balance_accounts_balance_account_id_payout_schedules(balance_account_id: str, body: BalanceAccountConfigurationRequest | BalanceAccountConfigurationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`, `body`
- **Params**: `balance_account_id` — path `balanceAccountId` · `body` — JSON body
- **Returns (parsed)**: `BalanceAccountConfiguration`
- **Returns (raw)**: `ApiResult[BalanceAccountConfiguration, PostBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody]`
- **Error**: `PostBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalanceAccountConfigurationRequest` | `adyen/models/balance_account_configuration_request.py` |
| `BalanceAccountConfigurationRequestDict` | `adyen/models/balance_account_configuration_request.py` |
| `BalanceAccountConfiguration` | `adyen/models/balance_account_configuration.py` |
| `PostBalanceAccountsBalanceAccountIdPayoutSchedulesErrorBody` | `adyen/errors/post_balance_accounts_balance_account_id_payout_schedules_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

