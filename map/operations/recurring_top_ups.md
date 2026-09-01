<!-- Generated file — do not edit; regenerated with the SDK. -->

# RecurringTopUps — operations

Accessor: `client.recurring_top_ups` · Source: `adyen/apis/recurring_top_ups.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.recurring_top_ups.delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id

- **Route**: `DELETE /balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId}`
- **Server**: `default13`
- **Signature**: `def delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(balance_account_id: str, top_up_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`, `top_up_id`
- **Params**: `balance_account_id` — path `balanceAccountId` · `top_up_id` — path `topUpId`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, DeleteBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody]`
- **Error**: `DeleteBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody` | `adyen/errors/delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.recurring_top_ups.get_balance_accounts_balance_account_id_recurring_top_ups

- **Route**: `GET /balanceAccounts/{balanceAccountId}/recurringTopUps`
- **Server**: `default13`
- **Signature**: `def get_balance_accounts_balance_account_id_recurring_top_ups(balance_account_id: str, *, limit: int | None = 10, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`
- **Params**: `balance_account_id` — path `balanceAccountId` · `limit` — query · `cursor` — query
- **Returns (parsed)**: `RecurringTopUpsResult`
- **Returns (raw)**: `ApiResult[RecurringTopUpsResult, GetBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody]`
- **Error**: `GetBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [401, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RecurringTopUpsResult` | `adyen/models/recurring_top_ups_result.py` |
| `GetBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody` | `adyen/errors/get_balance_accounts_balance_account_id_recurring_top_ups_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.recurring_top_ups.patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id

- **Route**: `PATCH /balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId}`
- **Server**: `default13`
- **Signature**: `def patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(balance_account_id: str, top_up_id: str, body: PatchableCreateRecurringTopUp | PatchableCreateRecurringTopUpDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`, `top_up_id`, `body`
- **Params**: `balance_account_id` — path `balanceAccountId` · `top_up_id` — path `topUpId` · `body` — JSON body
- **Returns (parsed)**: `RecurringTopUp`
- **Returns (raw)**: `ApiResult[RecurringTopUp, PatchBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody]`
- **Error**: `PatchBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PatchableCreateRecurringTopUp` | `adyen/models/patchable_create_recurring_top_up.py` |
| `PatchableCreateRecurringTopUpDict` | `adyen/models/patchable_create_recurring_top_up.py` |
| `RecurringTopUp` | `adyen/models/recurring_top_up.py` |
| `PatchBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody` | `adyen/errors/patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

### client.recurring_top_ups.post_balance_accounts_balance_account_id_recurring_top_ups

- **Route**: `POST /balanceAccounts/{balanceAccountId}/recurringTopUps`
- **Server**: `default13`
- **Signature**: `def post_balance_accounts_balance_account_id_recurring_top_ups(balance_account_id: str, body: CreateRecurringTopUp | CreateRecurringTopUpDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `balance_account_id`, `body`
- **Params**: `balance_account_id` — path `balanceAccountId` · `body` — JSON body
- **Returns (parsed)**: `RecurringTopUp`
- **Returns (raw)**: `ApiResult[RecurringTopUp, PostBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody]`
- **Error**: `PostBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultErrorResponseEntity` [400, 401, 403, 422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateRecurringTopUp` | `adyen/models/create_recurring_top_up.py` |
| `CreateRecurringTopUpDict` | `adyen/models/create_recurring_top_up.py` |
| `RecurringTopUp` | `adyen/models/recurring_top_up.py` |
| `PostBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody` | `adyen/errors/post_balance_accounts_balance_account_id_recurring_top_ups_error.py` |
| `DefaultErrorResponseEntity` | `adyen/models/default_error_response_entity.py` |

