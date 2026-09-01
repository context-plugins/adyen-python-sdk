<!-- Generated file — do not edit; regenerated with the SDK. -->

# General — operations

Accessor: `client.general` · Source: `adyen/apis/general.py` · 41 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.general.post_accept_dispute

- **Route**: `POST /acceptDispute`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default22`
- **Signature**: `def post_accept_dispute(*, body: AcceptDisputeRequest | AcceptDisputeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AcceptDisputeResponse`
- **Returns (raw)**: `ApiResult[AcceptDisputeResponse, PostAcceptDisputeErrorBody]`
- **Error**: `PostAcceptDisputeErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AcceptDisputeRequest` | `adyen/models/accept_dispute_request.py` |
| `AcceptDisputeRequestDict` | `adyen/models/accept_dispute_request.py` |
| `AcceptDisputeResponse` | `adyen/models/accept_dispute_response.py` |
| `PostAcceptDisputeErrorBody` | `adyen/errors/post_accept_dispute_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_account_holder_balance

- **Route**: `POST /accountHolderBalance`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default16`
- **Signature**: `def post_account_holder_balance(*, body: CloseAccountHolderRequest | CloseAccountHolderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountHolderBalanceResponse`
- **Returns (raw)**: `ApiResult[AccountHolderBalanceResponse, PostAccountHolderBalanceErrorBody]`
- **Error**: `PostAccountHolderBalanceErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CloseAccountHolderRequest` | `adyen/models/close_account_holder_request.py` |
| `CloseAccountHolderRequestDict` | `adyen/models/close_account_holder_request.py` |
| `AccountHolderBalanceResponse` | `adyen/models/account_holder_balance_response.py` |
| `PostAccountHolderBalanceErrorBody` | `adyen/errors/post_account_holder_balance_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_account_holder_transaction_list

- **Route**: `POST /accountHolderTransactionList`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default16`
- **Signature**: `def post_account_holder_transaction_list(*, body: AccountHolderTransactionListRequest | AccountHolderTransactionListRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountHolderTransactionListResponse`
- **Returns (raw)**: `ApiResult[AccountHolderTransactionListResponse, PostAccountHolderTransactionListErrorBody]`
- **Error**: `PostAccountHolderTransactionListErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountHolderTransactionListRequest` | `adyen/models/account_holder_transaction_list_request.py` |
| `AccountHolderTransactionListRequestDict` | `adyen/models/account_holder_transaction_list_request.py` |
| `AccountHolderTransactionListResponse` | `adyen/models/account_holder_transaction_list_response.py` |
| `PostAccountHolderTransactionListErrorBody` | `adyen/errors/post_account_holder_transaction_list_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_assign_terminals

- **Route**: `POST /assignTerminals`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default28`
- **Signature**: `def post_assign_terminals(*, body: AssignTerminalsRequest | AssignTerminalsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssignTerminalsResponse`
- **Returns (raw)**: `ApiResult[AssignTerminalsResponse, PostAssignTerminalsErrorBody]`
- **Error**: `PostAssignTerminalsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AssignTerminalsRequest` | `adyen/models/assign_terminals_request.py` |
| `AssignTerminalsRequestDict` | `adyen/models/assign_terminals_request.py` |
| `AssignTerminalsResponse` | `adyen/models/assign_terminals_response.py` |
| `PostAssignTerminalsErrorBody` | `adyen/errors/post_assign_terminals_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_change_status

- **Route**: `POST /changeStatus`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default5`
- **Signature**: `def post_change_status(*, body: StoredValueStatusChangeRequest | StoredValueStatusChangeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StoredValueStatusChangeResponse`
- **Returns (raw)**: `ApiResult[StoredValueStatusChangeResponse, PostChangeStatusErrorBody]`
- **Error**: `PostChangeStatusErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StoredValueStatusChangeRequest` | `adyen/models/stored_value_status_change_request.py` |
| `StoredValueStatusChangeRequestDict` | `adyen/models/stored_value_status_change_request.py` |
| `StoredValueStatusChangeResponse` | `adyen/models/stored_value_status_change_response.py` |
| `PostChangeStatusErrorBody` | `adyen/errors/post_change_status_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_check_balance

- **Route**: `POST /checkBalance`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default5`
- **Signature**: `def post_check_balance(*, body: StoredValueBalanceCheckRequest | StoredValueBalanceCheckRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StoredValueBalanceCheckResponse`
- **Returns (raw)**: `ApiResult[StoredValueBalanceCheckResponse, PostCheckBalanceErrorBody]`
- **Error**: `PostCheckBalanceErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StoredValueBalanceCheckRequest` | `adyen/models/stored_value_balance_check_request.py` |
| `StoredValueBalanceCheckRequestDict` | `adyen/models/stored_value_balance_check_request.py` |
| `StoredValueBalanceCheckResponse` | `adyen/models/stored_value_balance_check_response.py` |
| `PostCheckBalanceErrorBody` | `adyen/errors/post_check_balance_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_create_notification_configuration

- **Route**: `POST /createNotificationConfiguration`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default12`
- **Signature**: `def post_create_notification_configuration(*, body: CreateNotificationConfigurationRequest | CreateNotificationConfigurationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetNotificationConfigurationResponse`
- **Returns (raw)**: `ApiResult[GetNotificationConfigurationResponse, PostCreateNotificationConfigurationErrorBody]`
- **Error**: `PostCreateNotificationConfigurationErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateNotificationConfigurationRequest` | `adyen/models/create_notification_configuration_request.py` |
| `CreateNotificationConfigurationRequestDict` | `adyen/models/create_notification_configuration_request.py` |
| `GetNotificationConfigurationResponse` | `adyen/models/get_notification_configuration_response.py` |
| `PostCreateNotificationConfigurationErrorBody` | `adyen/errors/post_create_notification_configuration_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_create_permit

- **Route**: `POST /createPermit`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default2`
- **Signature**: `def post_create_permit(*, body: CreatePermitRequest | CreatePermitRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreatePermitResult`
- **Returns (raw)**: `ApiResult[CreatePermitResult, PostCreatePermitErrorBody]`
- **Error**: `PostCreatePermitErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreatePermitRequest` | `adyen/models/create_permit_request.py` |
| `CreatePermitRequestDict` | `adyen/models/create_permit_request.py` |
| `CreatePermitResult` | `adyen/models/create_permit_result.py` |
| `PostCreatePermitErrorBody` | `adyen/errors/post_create_permit_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_create_test_card_ranges

- **Route**: `POST /createTestCardRanges`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default8`
- **Signature**: `def post_create_test_card_ranges(*, body: CreateTestCardRangesRequest | CreateTestCardRangesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateTestCardRangesResult`
- **Returns (raw)**: `ApiResult[CreateTestCardRangesResult, PostCreateTestCardRangesErrorBody]`
- **Error**: `PostCreateTestCardRangesErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateTestCardRangesRequest` | `adyen/models/create_test_card_ranges_request.py` |
| `CreateTestCardRangesRequestDict` | `adyen/models/create_test_card_ranges_request.py` |
| `CreateTestCardRangesResult` | `adyen/models/create_test_card_ranges_result.py` |
| `PostCreateTestCardRangesErrorBody` | `adyen/errors/post_create_test_card_ranges_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_debit_account_holder

- **Route**: `POST /debitAccountHolder`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default16`
- **Signature**: `def post_debit_account_holder(*, body: DebitAccountHolderRequest | DebitAccountHolderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DebitAccountHolderResponse`
- **Returns (raw)**: `ApiResult[DebitAccountHolderResponse, PostDebitAccountHolderErrorBody]`
- **Error**: `PostDebitAccountHolderErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DebitAccountHolderRequest` | `adyen/models/debit_account_holder_request.py` |
| `DebitAccountHolderRequestDict` | `adyen/models/debit_account_holder_request.py` |
| `DebitAccountHolderResponse` | `adyen/models/debit_account_holder_response.py` |
| `PostDebitAccountHolderErrorBody` | `adyen/errors/post_debit_account_holder_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_defend_dispute

- **Route**: `POST /defendDispute`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default22`
- **Signature**: `def post_defend_dispute(*, body: DefendDisputeRequest | DefendDisputeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DefendDisputeResponse`
- **Returns (raw)**: `ApiResult[DefendDisputeResponse, PostDefendDisputeErrorBody]`
- **Error**: `PostDefendDisputeErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DefendDisputeRequest` | `adyen/models/defend_dispute_request.py` |
| `DefendDisputeRequestDict` | `adyen/models/defend_dispute_request.py` |
| `DefendDisputeResponse` | `adyen/models/defend_dispute_response.py` |
| `PostDefendDisputeErrorBody` | `adyen/errors/post_defend_dispute_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_delete_dispute_defense_document

- **Route**: `POST /deleteDisputeDefenseDocument`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default22`
- **Signature**: `def post_delete_dispute_defense_document(*, body: DeleteDefenseDocumentRequest | DeleteDefenseDocumentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeleteDefenseDocumentResponse`
- **Returns (raw)**: `ApiResult[DeleteDefenseDocumentResponse, PostDeleteDisputeDefenseDocumentErrorBody]`
- **Error**: `PostDeleteDisputeDefenseDocumentErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteDefenseDocumentRequest` | `adyen/models/delete_defense_document_request.py` |
| `DeleteDefenseDocumentRequestDict` | `adyen/models/delete_defense_document_request.py` |
| `DeleteDefenseDocumentResponse` | `adyen/models/delete_defense_document_response.py` |
| `PostDeleteDisputeDefenseDocumentErrorBody` | `adyen/errors/post_delete_dispute_defense_document_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_delete_notification_configurations

- **Route**: `POST /deleteNotificationConfigurations`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default12`
- **Signature**: `def post_delete_notification_configurations(*, body: DeleteNotificationConfigurationRequest | DeleteNotificationConfigurationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenericResponse`
- **Returns (raw)**: `ApiResult[GenericResponse, PostDeleteNotificationConfigurationsErrorBody]`
- **Error**: `PostDeleteNotificationConfigurationsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteNotificationConfigurationRequest` | `adyen/models/delete_notification_configuration_request.py` |
| `DeleteNotificationConfigurationRequestDict` | `adyen/models/delete_notification_configuration_request.py` |
| `GenericResponse` | `adyen/models/generic_response.py` |
| `PostDeleteNotificationConfigurationsErrorBody` | `adyen/errors/post_delete_notification_configurations_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_disable

- **Route**: `POST /disable`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default2`
- **Signature**: `def post_disable(*, body: DisableRequest | DisableRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DisableResult`
- **Returns (raw)**: `ApiResult[DisableResult, PostDisableErrorBody]`
- **Error**: `PostDisableErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisableRequest` | `adyen/models/disable_request.py` |
| `DisableRequestDict` | `adyen/models/disable_request.py` |
| `DisableResult` | `adyen/models/disable_result.py` |
| `PostDisableErrorBody` | `adyen/errors/post_disable_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_disable_permit

- **Route**: `POST /disablePermit`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default2`
- **Signature**: `def post_disable_permit(*, body: DisablePermitRequest | DisablePermitRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DisablePermitResult`
- **Returns (raw)**: `ApiResult[DisablePermitResult, PostDisablePermitErrorBody]`
- **Error**: `PostDisablePermitErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisablePermitRequest` | `adyen/models/disable_permit_request.py` |
| `DisablePermitRequestDict` | `adyen/models/disable_permit_request.py` |
| `DisablePermitResult` | `adyen/models/disable_permit_result.py` |
| `PostDisablePermitErrorBody` | `adyen/errors/post_disable_permit_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_find_terminal

- **Route**: `POST /findTerminal`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default28`
- **Signature**: `def post_find_terminal(*, body: FindTerminalRequest | FindTerminalRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FindTerminalResponse`
- **Returns (raw)**: `ApiResult[FindTerminalResponse, PostFindTerminalErrorBody]`
- **Error**: `PostFindTerminalErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FindTerminalRequest` | `adyen/models/find_terminal_request.py` |
| `FindTerminalRequestDict` | `adyen/models/find_terminal_request.py` |
| `FindTerminalResponse` | `adyen/models/find_terminal_response.py` |
| `PostFindTerminalErrorBody` | `adyen/errors/post_find_terminal_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_get3ds_availability

- **Route**: `POST /get3dsAvailability`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default4`
- **Signature**: `def post_get3ds_availability(*, body: ThreeDsavailabilityRequest | ThreeDsavailabilityRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ThreeDsavailabilityResponse`
- **Returns (raw)**: `ApiResult[ThreeDsavailabilityResponse, PostGet3DsAvailabilityErrorBody]`
- **Error**: `PostGet3DsAvailabilityErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ThreeDsavailabilityRequest` | `adyen/models/three_dsavailability_request.py` |
| `ThreeDsavailabilityRequestDict` | `adyen/models/three_dsavailability_request.py` |
| `ThreeDsavailabilityResponse` | `adyen/models/three_dsavailability_response.py` |
| `PostGet3DsAvailabilityErrorBody` | `adyen/errors/post_get3_ds_availability_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_get_cost_estimate

- **Route**: `POST /getCostEstimate`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default4`
- **Signature**: `def post_get_cost_estimate(*, body: CostEstimateRequest | CostEstimateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CostEstimateResponse`
- **Returns (raw)**: `ApiResult[CostEstimateResponse, PostGetCostEstimateErrorBody]`
- **Error**: `PostGetCostEstimateErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CostEstimateRequest` | `adyen/models/cost_estimate_request.py` |
| `CostEstimateRequestDict` | `adyen/models/cost_estimate_request.py` |
| `CostEstimateResponse` | `adyen/models/cost_estimate_response.py` |
| `PostGetCostEstimateErrorBody` | `adyen/errors/post_get_cost_estimate_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_get_notification_configuration

- **Route**: `POST /getNotificationConfiguration`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default12`
- **Signature**: `def post_get_notification_configuration(*, body: GetNotificationConfigurationRequest | GetNotificationConfigurationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetNotificationConfigurationResponse`
- **Returns (raw)**: `ApiResult[GetNotificationConfigurationResponse, PostGetNotificationConfigurationErrorBody]`
- **Error**: `PostGetNotificationConfigurationErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetNotificationConfigurationRequest` | `adyen/models/get_notification_configuration_request.py` |
| `GetNotificationConfigurationRequestDict` | `adyen/models/get_notification_configuration_request.py` |
| `GetNotificationConfigurationResponse` | `adyen/models/get_notification_configuration_response.py` |
| `PostGetNotificationConfigurationErrorBody` | `adyen/errors/post_get_notification_configuration_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_get_notification_configuration_list

- **Route**: `POST /getNotificationConfigurationList`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default12`
- **Signature**: `def post_get_notification_configuration_list(*, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetNotificationConfigurationListResponse`
- **Returns (raw)**: `ApiResult[GetNotificationConfigurationListResponse, PostGetNotificationConfigurationListErrorBody]`
- **Error**: `PostGetNotificationConfigurationListErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetNotificationConfigurationListResponse` | `adyen/models/get_notification_configuration_list_response.py` |
| `PostGetNotificationConfigurationListErrorBody` | `adyen/errors/post_get_notification_configuration_list_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_get_stores_under_account

- **Route**: `POST /getStoresUnderAccount`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default28`
- **Signature**: `def post_get_stores_under_account(*, body: GetStoresUnderAccountRequest | GetStoresUnderAccountRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetStoresUnderAccountResponse`
- **Returns (raw)**: `ApiResult[GetStoresUnderAccountResponse, PostGetStoresUnderAccountErrorBody]`
- **Error**: `PostGetStoresUnderAccountErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetStoresUnderAccountRequest` | `adyen/models/get_stores_under_account_request.py` |
| `GetStoresUnderAccountRequestDict` | `adyen/models/get_stores_under_account_request.py` |
| `GetStoresUnderAccountResponse` | `adyen/models/get_stores_under_account_response.py` |
| `PostGetStoresUnderAccountErrorBody` | `adyen/errors/post_get_stores_under_account_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_get_terminal_details

- **Route**: `POST /getTerminalDetails`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default28`
- **Signature**: `def post_get_terminal_details(*, body: GetTerminalDetailsRequest | GetTerminalDetailsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetTerminalDetailsResponse`
- **Returns (raw)**: `ApiResult[GetTerminalDetailsResponse, PostGetTerminalDetailsErrorBody]`
- **Error**: `PostGetTerminalDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetTerminalDetailsRequest` | `adyen/models/get_terminal_details_request.py` |
| `GetTerminalDetailsRequestDict` | `adyen/models/get_terminal_details_request.py` |
| `GetTerminalDetailsResponse` | `adyen/models/get_terminal_details_response.py` |
| `PostGetTerminalDetailsErrorBody` | `adyen/errors/post_get_terminal_details_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_get_terminals_under_account

- **Route**: `POST /getTerminalsUnderAccount`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default28`
- **Signature**: `def post_get_terminals_under_account(*, body: GetTerminalsUnderAccountRequest | GetTerminalsUnderAccountRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetTerminalsUnderAccountResponse`
- **Returns (raw)**: `ApiResult[GetTerminalsUnderAccountResponse, PostGetTerminalsUnderAccountErrorBody]`
- **Error**: `PostGetTerminalsUnderAccountErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetTerminalsUnderAccountRequest` | `adyen/models/get_terminals_under_account_request.py` |
| `GetTerminalsUnderAccountRequestDict` | `adyen/models/get_terminals_under_account_request.py` |
| `GetTerminalsUnderAccountResponse` | `adyen/models/get_terminals_under_account_response.py` |
| `PostGetTerminalsUnderAccountErrorBody` | `adyen/errors/post_get_terminals_under_account_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_issue

- **Route**: `POST /issue`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default5`
- **Signature**: `def post_issue(*, body: StoredValueIssueRequest | StoredValueIssueRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StoredValueIssueResponse`
- **Returns (raw)**: `ApiResult[StoredValueIssueResponse, PostIssueErrorBody]`
- **Error**: `PostIssueErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StoredValueIssueRequest` | `adyen/models/stored_value_issue_request.py` |
| `StoredValueIssueRequestDict` | `adyen/models/stored_value_issue_request.py` |
| `StoredValueIssueResponse` | `adyen/models/stored_value_issue_response.py` |
| `PostIssueErrorBody` | `adyen/errors/post_issue_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_list_recurring_details

- **Route**: `POST /listRecurringDetails`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default2`
- **Signature**: `def post_list_recurring_details(*, body: RecurringDetailsRequest | RecurringDetailsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RecurringDetailsResult`
- **Returns (raw)**: `ApiResult[RecurringDetailsResult, PostListRecurringDetailsErrorBody]`
- **Error**: `PostListRecurringDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RecurringDetailsRequest` | `adyen/models/recurring_details_request.py` |
| `RecurringDetailsRequestDict` | `adyen/models/recurring_details_request.py` |
| `RecurringDetailsResult` | `adyen/models/recurring_details_result.py` |
| `PostListRecurringDetailsErrorBody` | `adyen/errors/post_list_recurring_details_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_load

- **Route**: `POST /load`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default5`
- **Signature**: `def post_load(*, body: StoredValueLoadRequest | StoredValueLoadRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StoredValueLoadResponse`
- **Returns (raw)**: `ApiResult[StoredValueLoadResponse, PostLoadErrorBody]`
- **Error**: `PostLoadErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StoredValueLoadRequest` | `adyen/models/stored_value_load_request.py` |
| `StoredValueLoadRequestDict` | `adyen/models/stored_value_load_request.py` |
| `StoredValueLoadResponse` | `adyen/models/stored_value_load_response.py` |
| `PostLoadErrorBody` | `adyen/errors/post_load_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_merge_balance

- **Route**: `POST /mergeBalance`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default5`
- **Signature**: `def post_merge_balance(*, body: StoredValueBalanceMergeRequest | StoredValueBalanceMergeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StoredValueBalanceMergeResponse`
- **Returns (raw)**: `ApiResult[StoredValueBalanceMergeResponse, PostMergeBalanceErrorBody]`
- **Error**: `PostMergeBalanceErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StoredValueBalanceMergeRequest` | `adyen/models/stored_value_balance_merge_request.py` |
| `StoredValueBalanceMergeRequestDict` | `adyen/models/stored_value_balance_merge_request.py` |
| `StoredValueBalanceMergeResponse` | `adyen/models/stored_value_balance_merge_response.py` |
| `PostMergeBalanceErrorBody` | `adyen/errors/post_merge_balance_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_notify_shopper

- **Route**: `POST /notifyShopper`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default2`
- **Signature**: `def post_notify_shopper(*, body: NotifyShopperRequest | NotifyShopperRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `NotifyShopperResult`
- **Returns (raw)**: `ApiResult[NotifyShopperResult, PostNotifyShopperErrorBody]`
- **Error**: `PostNotifyShopperErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `NotifyShopperRequest` | `adyen/models/notify_shopper_request.py` |
| `NotifyShopperRequestDict` | `adyen/models/notify_shopper_request.py` |
| `NotifyShopperResult` | `adyen/models/notify_shopper_result.py` |
| `PostNotifyShopperErrorBody` | `adyen/errors/post_notify_shopper_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_payout_account_holder

- **Route**: `POST /payoutAccountHolder`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default16`
- **Signature**: `def post_payout_account_holder(*, body: PayoutAccountHolderRequest | PayoutAccountHolderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PayoutAccountHolderResponse`
- **Returns (raw)**: `ApiResult[PayoutAccountHolderResponse, PostPayoutAccountHolderErrorBody]`
- **Error**: `PostPayoutAccountHolderErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PayoutAccountHolderRequest` | `adyen/models/payout_account_holder_request.py` |
| `PayoutAccountHolderRequestDict` | `adyen/models/payout_account_holder_request.py` |
| `PayoutAccountHolderResponse` | `adyen/models/payout_account_holder_response.py` |
| `PostPayoutAccountHolderErrorBody` | `adyen/errors/post_payout_account_holder_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_refund_funds_transfer

- **Route**: `POST /refundFundsTransfer`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default16`
- **Signature**: `def post_refund_funds_transfer(*, body: RefundFundsTransferRequest | RefundFundsTransferRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RefundFundsTransferResponse`
- **Returns (raw)**: `ApiResult[RefundFundsTransferResponse, PostRefundFundsTransferErrorBody]`
- **Error**: `PostRefundFundsTransferErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RefundFundsTransferRequest` | `adyen/models/refund_funds_transfer_request.py` |
| `RefundFundsTransferRequestDict` | `adyen/models/refund_funds_transfer_request.py` |
| `RefundFundsTransferResponse` | `adyen/models/refund_funds_transfer_response.py` |
| `PostRefundFundsTransferErrorBody` | `adyen/errors/post_refund_funds_transfer_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_refund_not_paid_out_transfers

- **Route**: `POST /refundNotPaidOutTransfers`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default16`
- **Signature**: `def post_refund_not_paid_out_transfers(*, body: RefundNotPaidOutTransfersRequest | RefundNotPaidOutTransfersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenericResponse`
- **Returns (raw)**: `ApiResult[GenericResponse, PostRefundNotPaidOutTransfersErrorBody]`
- **Error**: `PostRefundNotPaidOutTransfersErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RefundNotPaidOutTransfersRequest` | `adyen/models/refund_not_paid_out_transfers_request.py` |
| `RefundNotPaidOutTransfersRequestDict` | `adyen/models/refund_not_paid_out_transfers_request.py` |
| `GenericResponse` | `adyen/models/generic_response.py` |
| `PostRefundNotPaidOutTransfersErrorBody` | `adyen/errors/post_refund_not_paid_out_transfers_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_request_subject_erasure

- **Route**: `POST /requestSubjectErasure`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default6`
- **Signature**: `def post_request_subject_erasure(*, body: SubjectErasureByPspReferenceRequest | SubjectErasureByPspReferenceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SubjectErasureResponse`
- **Returns (raw)**: `ApiResult[SubjectErasureResponse, PostRequestSubjectErasureErrorBody]`
- **Error**: `PostRequestSubjectErasureErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubjectErasureByPspReferenceRequest` | `adyen/models/subject_erasure_by_psp_reference_request.py` |
| `SubjectErasureByPspReferenceRequestDict` | `adyen/models/subject_erasure_by_psp_reference_request.py` |
| `SubjectErasureResponse` | `adyen/models/subject_erasure_response.py` |
| `PostRequestSubjectErasureErrorBody` | `adyen/errors/post_request_subject_erasure_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_retrieve_applicable_defense_reasons

- **Route**: `POST /retrieveApplicableDefenseReasons`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default22`
- **Signature**: `def post_retrieve_applicable_defense_reasons(*, body: DefenseReasonsRequest | DefenseReasonsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DefenseReasonsResponse`
- **Returns (raw)**: `ApiResult[DefenseReasonsResponse, PostRetrieveApplicableDefenseReasonsErrorBody]`
- **Error**: `PostRetrieveApplicableDefenseReasonsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DefenseReasonsRequest` | `adyen/models/defense_reasons_request.py` |
| `DefenseReasonsRequestDict` | `adyen/models/defense_reasons_request.py` |
| `DefenseReasonsResponse` | `adyen/models/defense_reasons_response.py` |
| `PostRetrieveApplicableDefenseReasonsErrorBody` | `adyen/errors/post_retrieve_applicable_defense_reasons_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_schedule_account_updater

- **Route**: `POST /scheduleAccountUpdater`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default2`
- **Signature**: `def post_schedule_account_updater(*, body: ScheduleAccountUpdaterRequest | ScheduleAccountUpdaterRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ScheduleAccountUpdaterResult`
- **Returns (raw)**: `ApiResult[ScheduleAccountUpdaterResult, PostScheduleAccountUpdaterErrorBody]`
- **Error**: `PostScheduleAccountUpdaterErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ScheduleAccountUpdaterRequest` | `adyen/models/schedule_account_updater_request.py` |
| `ScheduleAccountUpdaterRequestDict` | `adyen/models/schedule_account_updater_request.py` |
| `ScheduleAccountUpdaterResult` | `adyen/models/schedule_account_updater_result.py` |
| `PostScheduleAccountUpdaterErrorBody` | `adyen/errors/post_schedule_account_updater_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

### client.general.post_sessions3

- **Route**: `POST /sessions`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default27`
- **Signature**: `def post_sessions3(*, body: CreateSessionRequest | CreateSessionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CertificateLoadingResponse`
- **Returns (raw)**: `ApiResult[CertificateLoadingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateSessionRequest` | `adyen/models/create_session_request.py` |
| `CreateSessionRequestDict` | `adyen/models/create_session_request.py` |
| `CertificateLoadingResponse` | `adyen/models/certificate_loading_response.py` |

### client.general.post_setup_beneficiary

- **Route**: `POST /setupBeneficiary`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default16`
- **Signature**: `def post_setup_beneficiary(*, body: SetupBeneficiaryRequest | SetupBeneficiaryRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenericResponse`
- **Returns (raw)**: `ApiResult[GenericResponse, PostSetupBeneficiaryErrorBody]`
- **Error**: `PostSetupBeneficiaryErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetupBeneficiaryRequest` | `adyen/models/setup_beneficiary_request.py` |
| `SetupBeneficiaryRequestDict` | `adyen/models/setup_beneficiary_request.py` |
| `GenericResponse` | `adyen/models/generic_response.py` |
| `PostSetupBeneficiaryErrorBody` | `adyen/errors/post_setup_beneficiary_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_supply_defense_document

- **Route**: `POST /supplyDefenseDocument`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default22`
- **Signature**: `def post_supply_defense_document(*, body: SupplyDefenseDocumentRequest | SupplyDefenseDocumentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SupplyDefenseDocumentResponse`
- **Returns (raw)**: `ApiResult[SupplyDefenseDocumentResponse, PostSupplyDefenseDocumentErrorBody]`
- **Error**: `PostSupplyDefenseDocumentErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SupplyDefenseDocumentRequest` | `adyen/models/supply_defense_document_request.py` |
| `SupplyDefenseDocumentRequestDict` | `adyen/models/supply_defense_document_request.py` |
| `SupplyDefenseDocumentResponse` | `adyen/models/supply_defense_document_response.py` |
| `PostSupplyDefenseDocumentErrorBody` | `adyen/errors/post_supply_defense_document_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_test_notification_configuration

- **Route**: `POST /testNotificationConfiguration`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default12`
- **Signature**: `def post_test_notification_configuration(*, body: TestNotificationConfigurationRequest | TestNotificationConfigurationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TestNotificationConfigurationResponse`
- **Returns (raw)**: `ApiResult[TestNotificationConfigurationResponse, PostTestNotificationConfigurationErrorBody]`
- **Error**: `PostTestNotificationConfigurationErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TestNotificationConfigurationRequest` | `adyen/models/test_notification_configuration_request.py` |
| `TestNotificationConfigurationRequestDict` | `adyen/models/test_notification_configuration_request.py` |
| `TestNotificationConfigurationResponse` | `adyen/models/test_notification_configuration_response.py` |
| `PostTestNotificationConfigurationErrorBody` | `adyen/errors/post_test_notification_configuration_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_transfer_funds

- **Route**: `POST /transferFunds`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default16`
- **Signature**: `def post_transfer_funds(*, body: TransferFundsRequest | TransferFundsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferFundsResponse`
- **Returns (raw)**: `ApiResult[TransferFundsResponse, PostTransferFundsErrorBody]`
- **Error**: `PostTransferFundsErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransferFundsRequest` | `adyen/models/transfer_funds_request.py` |
| `TransferFundsRequestDict` | `adyen/models/transfer_funds_request.py` |
| `TransferFundsResponse` | `adyen/models/transfer_funds_response.py` |
| `PostTransferFundsErrorBody` | `adyen/errors/post_transfer_funds_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_update_notification_configuration

- **Route**: `POST /updateNotificationConfiguration`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default12`
- **Signature**: `def post_update_notification_configuration(*, body: UpdateNotificationConfigurationRequest | UpdateNotificationConfigurationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetNotificationConfigurationResponse`
- **Returns (raw)**: `ApiResult[GetNotificationConfigurationResponse, PostUpdateNotificationConfigurationErrorBody]`
- **Error**: `PostUpdateNotificationConfigurationErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError1` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateNotificationConfigurationRequest` | `adyen/models/update_notification_configuration_request.py` |
| `UpdateNotificationConfigurationRequestDict` | `adyen/models/update_notification_configuration_request.py` |
| `GetNotificationConfigurationResponse` | `adyen/models/get_notification_configuration_response.py` |
| `PostUpdateNotificationConfigurationErrorBody` | `adyen/errors/post_update_notification_configuration_error.py` |
| `ServiceError1` | `adyen/models/service_error1.py` |

### client.general.post_void_transaction

- **Route**: `POST /voidTransaction`
- **Auth**: `basic_auth` OR `api_key_auth`
- **Server**: `default5`
- **Signature**: `def post_void_transaction(*, body: StoredValueVoidRequest | StoredValueVoidRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StoredValueVoidResponse`
- **Returns (raw)**: `ApiResult[StoredValueVoidResponse, PostVoidTransactionErrorBody]`
- **Error**: `PostVoidTransactionErrorBody` — **Case A (typed)**
- **Error arms**: `ServiceError` [400, 401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StoredValueVoidRequest` | `adyen/models/stored_value_void_request.py` |
| `StoredValueVoidRequestDict` | `adyen/models/stored_value_void_request.py` |
| `StoredValueVoidResponse` | `adyen/models/stored_value_void_response.py` |
| `PostVoidTransactionErrorBody` | `adyen/errors/post_void_transaction_error.py` |
| `ServiceError` | `adyen/models/service_error.py` |

