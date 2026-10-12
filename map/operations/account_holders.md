<!-- Generated file — do not edit; regenerated with the SDK. -->

# AccountHolders — operations

Accessor: `client.account_holders` · Source: `adyen/apis/account_holders.py` · 16 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account_holders.get_account_holders_id

- **Route**: `GET /accountHolders/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_account_holders_id(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `AccountHolder`
- **Returns (raw)**: `ApiResult[AccountHolder, GetAccountHoldersIdErrorBody]`
- **Error**: `GetAccountHoldersIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountHolder` | `adyen/models/account_holder.py` |
| `GetAccountHoldersIdErrorBody` | `adyen/errors/get_account_holders_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_holders.get_account_holders_id_balance_accounts

- **Route**: `GET /accountHolders/{id}/balanceAccounts`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_account_holders_id_balance_accounts(id_: str, *, offset: int | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `offset` — query · `limit` — query
- **Returns (parsed)**: `PaginatedBalanceAccountsResponse`
- **Returns (raw)**: `ApiResult[PaginatedBalanceAccountsResponse, GetAccountHoldersIdBalanceAccountsErrorBody]`
- **Error**: `GetAccountHoldersIdBalanceAccountsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaginatedBalanceAccountsResponse` | `adyen/models/paginated_balance_accounts_response.py` |
| `GetAccountHoldersIdBalanceAccountsErrorBody` | `adyen/errors/get_account_holders_id_balance_accounts_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_holders.get_account_holders_id_tax_form_summary

- **Route**: `GET /accountHolders/{id}/taxFormSummary`
- **Server**: `default13`
- **Signature**: `def get_account_holders_id_tax_form_summary(id_: str, form_type: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `form_type`
- **Params**: `id_` — path `id` · `form_type` — query `formType`
- **Returns (parsed)**: `TaxFormSummaryResponse`
- **Returns (raw)**: `ApiResult[TaxFormSummaryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TaxFormSummaryResponse` | `adyen/models/tax_form_summary_response.py` |

### client.account_holders.get_account_holders_id_tax_forms

- **Route**: `GET /accountHolders/{id}/taxForms`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_account_holders_id_tax_forms(id_: str, form_type: FormTypeOrStr, year: int, *, legal_entity_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `form_type`, `year`
- **Params**: `id_` — path `id` · `form_type` — query `formType` · `year` — query · `legal_entity_id` — query `legalEntityId`
- **Returns (parsed)**: `GetTaxFormResponse1`
- **Returns (raw)**: `ApiResult[GetTaxFormResponse1, GetAccountHoldersIdTaxFormsErrorBody]`
- **Error**: `GetAccountHoldersIdTaxFormsErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormTypeOrStr` | `adyen/models/enums/form_type.py` |
| `GetTaxFormResponse1` | `adyen/models/get_tax_form_response1.py` |
| `GetAccountHoldersIdTaxFormsErrorBody` | `adyen/errors/get_account_holders_id_tax_forms_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_holders.get_account_holders_id_transaction_rules

- **Route**: `GET /accountHolders/{id}/transactionRules`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def get_account_holders_id_transaction_rules(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `TransactionRulesResponse`
- **Returns (raw)**: `ApiResult[TransactionRulesResponse, GetAccountHoldersIdTransactionRulesErrorBody]`
- **Error**: `GetAccountHoldersIdTransactionRulesErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransactionRulesResponse` | `adyen/models/transaction_rules_response.py` |
| `GetAccountHoldersIdTransactionRulesErrorBody` | `adyen/errors/get_account_holders_id_transaction_rules_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_holders.patch_account_holders_id

- **Route**: `PATCH /accountHolders/{id}`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def patch_account_holders_id(id_: str, *, body: AccountHolderUpdateRequest | AccountHolderUpdateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `AccountHolder`
- **Returns (raw)**: `ApiResult[AccountHolder, PatchAccountHoldersIdErrorBody]`
- **Error**: `PatchAccountHoldersIdErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountHolderUpdateRequest` | `adyen/models/account_holder_update_request.py` |
| `AccountHolderUpdateRequestDict` | `adyen/models/account_holder_update_request.py` |
| `AccountHolder` | `adyen/models/account_holder.py` |
| `PatchAccountHoldersIdErrorBody` | `adyen/errors/patch_account_holders_id_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_holders.post_account_holders

- **Route**: `POST /accountHolders`
- **Auth**: `client_key` OR `basic_auth` OR `api_key_auth`
- **Server**: `default13`
- **Signature**: `def post_account_holders(*, body: AccountHolderInfo | AccountHolderInfoDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountHolder`
- **Returns (raw)**: `ApiResult[AccountHolder, PostAccountHoldersErrorBody]`
- **Error**: `PostAccountHoldersErrorBody` — **Case A (typed)**
- **Error arms**: `RestServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountHolderInfo` | `adyen/models/account_holder_info.py` |
| `AccountHolderInfoDict` | `adyen/models/account_holder_info.py` |
| `AccountHolder` | `adyen/models/account_holder.py` |
| `PostAccountHoldersErrorBody` | `adyen/errors/post_account_holders_error.py` |
| `RestServiceError` | `adyen/models/rest_service_error.py` |

### client.account_holders.post_close_account_holder

- **Route**: `POST /closeAccountHolder`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_close_account_holder(*, body: CloseAccountHolderRequest | CloseAccountHolderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CloseAccountHolderResponse`
- **Returns (raw)**: `ApiResult[CloseAccountHolderResponse, PostCloseAccountHolderErrorBody]`
- **Error**: `PostCloseAccountHolderErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CloseAccountHolderRequest` | `adyen/models/close_account_holder_request.py` |
| `CloseAccountHolderRequestDict` | `adyen/models/close_account_holder_request.py` |
| `CloseAccountHolderResponse` | `adyen/models/close_account_holder_response.py` |
| `PostCloseAccountHolderErrorBody` | `adyen/errors/post_close_account_holder_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.account_holders.post_close_stores

- **Route**: `POST /closeStores`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_close_stores(*, body: CloseStoresRequest | CloseStoresRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenericResponse`
- **Returns (raw)**: `ApiResult[GenericResponse, PostCloseStoresErrorBody]`
- **Error**: `PostCloseStoresErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CloseStoresRequest` | `adyen/models/close_stores_request.py` |
| `CloseStoresRequestDict` | `adyen/models/close_stores_request.py` |
| `GenericResponse` | `adyen/models/generic_response.py` |
| `PostCloseStoresErrorBody` | `adyen/errors/post_close_stores_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.account_holders.post_create_account_holder

- **Route**: `POST /createAccountHolder`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_create_account_holder(*, body: CreateAccountHolderRequest | CreateAccountHolderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateAccountHolderResponse`
- **Returns (raw)**: `ApiResult[CreateAccountHolderResponse, PostCreateAccountHolderErrorBody]`
- **Error**: `PostCreateAccountHolderErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateAccountHolderRequest` | `adyen/models/create_account_holder_request.py` |
| `CreateAccountHolderRequestDict` | `adyen/models/create_account_holder_request.py` |
| `CreateAccountHolderResponse` | `adyen/models/create_account_holder_response.py` |
| `PostCreateAccountHolderErrorBody` | `adyen/errors/post_create_account_holder_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.account_holders.post_get_account_holder

- **Route**: `POST /getAccountHolder`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_get_account_holder(*, body: GetAccountHolderRequest | GetAccountHolderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetAccountHolderResponse`
- **Returns (raw)**: `ApiResult[GetAccountHolderResponse, PostGetAccountHolderErrorBody]`
- **Error**: `PostGetAccountHolderErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAccountHolderRequest` | `adyen/models/get_account_holder_request.py` |
| `GetAccountHolderRequestDict` | `adyen/models/get_account_holder_request.py` |
| `GetAccountHolderResponse` | `adyen/models/get_account_holder_response.py` |
| `PostGetAccountHolderErrorBody` | `adyen/errors/post_get_account_holder_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.account_holders.post_get_tax_form

- **Route**: `POST /getTaxForm`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_get_tax_form(*, body: GetTaxFormRequest | GetTaxFormRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetTaxFormResponse`
- **Returns (raw)**: `ApiResult[GetTaxFormResponse, PostGetTaxFormErrorBody]`
- **Error**: `PostGetTaxFormErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetTaxFormRequest` | `adyen/models/get_tax_form_request.py` |
| `GetTaxFormRequestDict` | `adyen/models/get_tax_form_request.py` |
| `GetTaxFormResponse` | `adyen/models/get_tax_form_response.py` |
| `PostGetTaxFormErrorBody` | `adyen/errors/post_get_tax_form_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.account_holders.post_suspend_account_holder

- **Route**: `POST /suspendAccountHolder`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_suspend_account_holder(*, body: SuspendAccountHolderRequest | SuspendAccountHolderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SuspendAccountHolderResponse`
- **Returns (raw)**: `ApiResult[SuspendAccountHolderResponse, PostSuspendAccountHolderErrorBody]`
- **Error**: `PostSuspendAccountHolderErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SuspendAccountHolderRequest` | `adyen/models/suspend_account_holder_request.py` |
| `SuspendAccountHolderRequestDict` | `adyen/models/suspend_account_holder_request.py` |
| `SuspendAccountHolderResponse` | `adyen/models/suspend_account_holder_response.py` |
| `PostSuspendAccountHolderErrorBody` | `adyen/errors/post_suspend_account_holder_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.account_holders.post_un_suspend_account_holder

- **Route**: `POST /unSuspendAccountHolder`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_un_suspend_account_holder(*, body: UnSuspendAccountHolderRequest | UnSuspendAccountHolderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UnSuspendAccountHolderResponse`
- **Returns (raw)**: `ApiResult[UnSuspendAccountHolderResponse, PostUnSuspendAccountHolderErrorBody]`
- **Error**: `PostUnSuspendAccountHolderErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UnSuspendAccountHolderRequest` | `adyen/models/un_suspend_account_holder_request.py` |
| `UnSuspendAccountHolderRequestDict` | `adyen/models/un_suspend_account_holder_request.py` |
| `UnSuspendAccountHolderResponse` | `adyen/models/un_suspend_account_holder_response.py` |
| `PostUnSuspendAccountHolderErrorBody` | `adyen/errors/post_un_suspend_account_holder_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.account_holders.post_update_account_holder

- **Route**: `POST /updateAccountHolder`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_update_account_holder(*, body: UpdateAccountHolderRequest | UpdateAccountHolderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UpdateAccountHolderResponse`
- **Returns (raw)**: `ApiResult[UpdateAccountHolderResponse, PostUpdateAccountHolderErrorBody]`
- **Error**: `PostUpdateAccountHolderErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateAccountHolderRequest` | `adyen/models/update_account_holder_request.py` |
| `UpdateAccountHolderRequestDict` | `adyen/models/update_account_holder_request.py` |
| `UpdateAccountHolderResponse` | `adyen/models/update_account_holder_response.py` |
| `PostUpdateAccountHolderErrorBody` | `adyen/errors/post_update_account_holder_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.account_holders.post_update_account_holder_state

- **Route**: `POST /updateAccountHolderState`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default10`
- **Signature**: `def post_update_account_holder_state(*, body: UpdateAccountHolderStateRequest | UpdateAccountHolderStateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetAccountHolderStatusResponse`
- **Returns (raw)**: `ApiResult[GetAccountHolderStatusResponse, PostUpdateAccountHolderStateErrorBody]`
- **Error**: `PostUpdateAccountHolderStateErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateAccountHolderStateRequest` | `adyen/models/update_account_holder_state_request.py` |
| `UpdateAccountHolderStateRequestDict` | `adyen/models/update_account_holder_state_request.py` |
| `GetAccountHolderStatusResponse` | `adyen/models/get_account_holder_status_response.py` |
| `PostUpdateAccountHolderStateErrorBody` | `adyen/errors/post_update_account_holder_state_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

